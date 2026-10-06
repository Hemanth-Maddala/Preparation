"""
Project 08 - ReAct Agent
========================
A ReAct (Reason + Act) style agent built manually so you can SEE
the loop:  Reason -> Act -> Observe -> Reason -> ...

Flow:
   START -> agent -> (tools or END) -> END

- agent node: calls the LLM. If the reply has tool_calls, it "Acts".
- tools node: ToolNode runs the tool, producing the "Observe" step.
- The result (ToolMessage) goes back to agent, which "Reasons" again.
- Loop ends when the LLM answers without requesting a tool.

The LLM is REAL - Gemini, with the key loaded from .env
(no hardcoded keys, no mock).

Setup:
  Copy .env.example to .env and set your key:
    GEMINI_API_KEY=your_gemini_api_key

Run:
  python main.py
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


# ---------- Tools ----------

@tool
def calculator(expression: str) -> str:
    """Evaluate a simple arithmetic expression like '2+2'."""
    return str(eval(expression, {"__builtins__": {}}))


@tool
def weather(city: str) -> str:
    """Return a mock weather report for a city."""
    return f"Sunny, 28C in {city}"


TOOLS = [calculator, weather]


# ---------- Real LLM (Gemini, key from .env) ----------

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


# ---------- State ----------

class State(TypedDict):
    messages: Annotated[list, add_messages]


# ---------- Nodes ----------

def agent(state: State):
    # REASON: ask the model what to do next.
    response = llm.invoke(state["messages"])
    return {"messages": [response]}


def should_continue(state: State) -> Literal["tools", "__end__"]:
    # Look at the last message: did the model ask for a tool?
    last = state["messages"][-1]
    if getattr(last, "tool_calls", None):
        return "tools"   # ACT: run the tool, then observe
    return END           # done: final answer produced


# ---------- Build ----------

builder = StateGraph(State)
builder.add_node("agent", agent)
builder.add_node("tools", ToolNode(TOOLS))

builder.add_edge(START, "agent")
# Conditional routing closes the ReAct loop: agent -> tools -> agent -> ...
builder.add_conditional_edges("agent", should_continue, {"tools": "tools", END: END})
builder.add_edge("tools", "agent")

app = builder.compile()

if __name__ == "__main__":
    for question in ["What is the weather in Paris?", "What is 2+2?", "Hi there"]:
        result = app.invoke({"messages": [HumanMessage(content=question)]})
        print(f"\nQ: {question}")
        for m in result["messages"]:
            print(f"   {type(m).__name__}: {m.content or '(tool call)'}")
