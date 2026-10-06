"""
llm.py - Real Gemini LLM using the current Google GenAI SDK
============================================================
This project uses the NEW Google GenAI Python SDK (package `google-genai`):

    from google import genai

    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

The API key and the model come from ENVIRONMENT VARIABLES loaded from `.env`
via `load_dotenv()`. Nothing is hardcoded. `.env.example` shows the format:

    GEMINI_API_KEY=your_key
    GEMINI_MODEL=gemini-2.5-flash

This file exposes one small class, `AgentLLM`, that:
  1. wraps the Gemini client,
  2. translates LangGraph messages <-> Gemini contents,
  3. turns the model's function calls into LangGraph `tool_calls`
     that LangGraph's ToolNode can execute.

So LangGraph code can call `llm.invoke(messages)` just like any chat model.
"""

import os

from dotenv import load_dotenv
from google import genai
from google.genai import types
from langchain_core.messages import AIMessage, BaseMessage, HumanMessage, SystemMessage, ToolMessage

load_dotenv()

MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

# GenAI Schema rejects extra JSON-schema keys (like "title") that
# LangChain adds to its tool schemas, so we only keep the ones it accepts.
_ALLOWED_SCHEMA_KEYS = {
    "type", "format", "description", "nullable", "enum", "default",
    "items", "properties", "required", "anyOf", "example", "pattern",
}


def _clean_schema(node):
    """Recursively strip keys the GenAI SDK does not allow from a JSON schema."""
    if isinstance(node, dict):
        out = {}
        for key, value in node.items():
            if key not in _ALLOWED_SCHEMA_KEYS:
                continue
            if key == "properties":
                out[key] = {name: _clean_schema(schema) for name, schema in value.items()}
            else:
                out[key] = _clean_schema(value)
        return out
    if isinstance(node, list):
        return [_clean_schema(item) for item in node]
    return node


def _to_function_declarations(tools):
    """Turn LangGraph tools into Gemini FunctionDeclaration schemas."""
    return [
        types.FunctionDeclaration(
            name=tool.name,
            description=tool.description,
            parameters=_clean_schema(tool.args_schema.model_json_schema()),
        )
        for tool in tools
    ]


def _to_content(message: BaseMessage):
    """Translate one LangGraph message into a Gemini Content."""
    if isinstance(message, HumanMessage):
        return types.Content(role="user", parts=[types.Part(text=message.content)])
    if isinstance(message, AIMessage):
        parts = []
        if message.content:
            parts.append(types.Part(text=message.content))
        for call in message.tool_calls or []:
            parts.append(types.Part(function_call=types.FunctionCall(
                name=call["name"], args=call["args"], id=call["id"])))
        return types.Content(role="model", parts=parts)
    if isinstance(message, ToolMessage):
        return types.Content(role="user", parts=[types.Part(function_response=types.FunctionResponse(
            name=message.name or "", id=message.tool_call_id,
            response={"result": message.content}))])
    raise TypeError(f"Unsupported message type: {type(message).__name__}")


def _to_contents(messages):
    """Translate a list of messages, merging consecutive same-role contents."""
    result = []
    for message in messages:
        if isinstance(message, SystemMessage):
            continue  # system instructions are handled separately
        content = _to_content(message)
        if result and result[-1].role == content.role:
            result[-1].parts.extend(content.parts)
        else:
            result.append(content)
    return result


def _to_ai_message(response) -> AIMessage:
    """Translate a Gemini generate_content response into an AIMessage."""
    if not response.candidates or not response.candidates[0].content:
        raise RuntimeError("Gemini returned no content.")
    parts = response.candidates[0].content.parts
    text = "".join(part.text for part in parts if part.text) or ""
    tool_calls = []
    for part in parts:
        if part.function_call:
            tool_calls.append({
                "name": part.function_call.name,
                "args": dict(part.function_call.args or {}),
                "id": part.function_call.id or f"call_{len(tool_calls) + 1}",
            })
    return AIMessage(content=text, tool_calls=tool_calls)


class AgentLLM:
    """The agent's brain: a real Gemini model that can decide to call tools."""

    def __init__(self, tools=None, model=None):
        key = os.getenv("GEMINI_API_KEY")
        if not key:
            raise SystemExit(
                "GEMINI_API_KEY not found. Copy .env.example to .env and "
                "set GEMINI_API_KEY=<your key>, then run again."
            )
        self.client = genai.Client(api_key=key)
        self.model = model or MODEL
        if tools:
            self.tools = [types.Tool(function_declarations=_to_function_declarations(tools))]
        else:
            self.tools = None

    def invoke(self, messages, system=None):
        """`messages`: list of LangGraph messages.
        `system`: optional system instruction string.
        Returns an AIMessage (a normal answer or a tool call)."""
        system_text = system or ""
        for message in messages:
            if isinstance(message, SystemMessage):
                system_text += ("\n" if system_text else "") + message.content

        config = types.GenerateContentConfig(tools=self.tools)
        if system_text:
            config.system_instruction = system_text

        response = self.client.models.generate_content(
            model=self.model,
            contents=_to_contents(messages),
            config=config,
        )
        return _to_ai_message(response)
