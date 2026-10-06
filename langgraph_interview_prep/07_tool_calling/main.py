"""
Project 07 - Tool Calling
=========================
Give an agent the ability to call tools. The "agent" decides whether
a tool is needed, ToolNode executes the tool, and the result comes
back to the agent as a ToolMessage.

The tools (calculator / weather) are deterministic helpers, but the
DECISION is made by a REAL LLM - Gemini.

Setup:
  Copy .env.example to .env and set your key:
    GEMINI_API_KEY=your_gemini_api_key

Run:  python main.py
"""

import os
from typing import Annotated, Literal, TypedDict
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage
from langchain_core.tools import tool
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode
from dotenv import load_dotenv

load_dotenv()  # loads GEMINI_API_KEY from .env (never hardcode keys)


# ---------- 1. Define tools (real Python functions) ----------

@tool
def calculator(expression: str) -> str:
    """Evaluate a simple arithmetic expression like '2+2'."""
    return str(eval(expression, {"__builtins__": {}}))


@tool
def weather(city: str) -> str:
    """Return a mock weather report for a city."""
    return f"Sunny, 28C in {city}"


TOOLS = [calculator, weather]


# ---------- 2. Real LLM (Gemini, key from .env) ----------

def get_llm():
    key = os.getenv("GEMINI_API_KEY")
    if not key:
        raise SystemExit(
            "GEMINI_API_KEY not found. Copy .env.example to .env and "
            "set GEMINI_API_KEY=<your key>, then run again."
        )
    from langchain_google_genai import ChatGoogleGenerativeAI
    print("[llm] Using Gemini")
    return ChatGoogleGenerativeAI(
        model=os.getenv("GEMINI_MODEL", "gemini-2.5-flash"),
        api_key=key,
        temperature=0,
    ).bind_tools(TOOLS)


llm = get_llm()


# ---------- 3. State ----------

class State(TypedDict):
    messages: Annotated[list, add_messages]  # append-only message list


# ---------- 4. Nodes ----------

def agent(state: State):
    """Call the LLM. The returned message either contains a tool_call
    or is a normal answer."""
    response = llm.invoke(state["messages"])
    return {"messages": [response]}


def should_use_tool(state: State) -> Literal["tools", "__end__"]:
    last = state["messages"][-1]
    return "tools" if getattr(last, "tool_calls", None) else "__end__"


# ---------- 5. Build graph ----------

builder = StateGraph(State)
builder.add_node("agent", agent)
builder.add_node("tools", ToolNode(TOOLS))  # executes tool calls

builder.add_edge(START, "agent")
# If the agent asked for a tool -> run tools; otherwise we are done.
builder.add_conditional_edges("agent", should_use_tool, {"tools": "tools", END: END})
# After the tool runs, send the result back to the agent.
builder.add_edge("tools", "agent")

app = builder.compile()

if __name__ == "__main__":
    for question in ["What is 2+2?", "What is the weather in Paris?", "Hello"]:
        result = app.invoke({"messages": [HumanMessage(content=question)]})
        print(f"\nQ: {question}")
        print(f"A: {result['messages'][-1].content}")
