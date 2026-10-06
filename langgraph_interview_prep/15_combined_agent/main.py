"""
Project 15 - Combined Agent (AI Research Assistant)
===================================================
One small agent that combines everything learned so far:
  - State + nodes + edges
  - Conditional routing (tool loop or stop)
  - Tools (search + calculator)
  - ReAct loop (reason -> act -> observe)
  - Checkpointing / memory (thread_id)
  - Loop safety (max iterations)
  - Final response

Flow:
   START -> agent -> (tools or END) -> END     (tools -> agent again)

The LLM is REAL - Gemini, with the key loaded from .env
(no hardcoded keys, no mock).

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
from langgraph.checkpoint.memory import MemorySaver
from dotenv import load_dotenv

load_dotenv()  # loads GEMINI_API_KEY from .env (never hardcode keys)

MAX_ITERATIONS = 4


# ---------- Tools ----------

@tool
def search_knowledge(query: str) -> str:
    """Mock web search over a small knowledge base."""
    knowledge = {
        "langgraph": "LangGraph is a library for building stateful LLM agents as graphs.",
        "react": "ReAct = Reason + Act: alternate thinking and tool calls.",
    }
    for key, value in knowledge.items():
        if key in query.lower():
            return value
    return f"No results for '{query}'."


@tool
def calculator(expression: str) -> str:
    """Evaluate a simple arithmetic expression like '2+2'."""
    return str(eval(expression, {"__builtins__": {}}))


TOOLS = [search_knowledge, calculator]


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


# ---------- State (messages + a loop counter) ----------

class State(TypedDict):
    messages: Annotated[list, add_messages]
    iterations: int


# ---------- Nodes ----------

def agent(state: State):
    print(f">>> agent (iteration {state['iterations'] + 1})")
    response = llm.invoke(state["messages"])
    return {"messages": [response], "iterations": state["iterations"] + 1}


def should_continue(state: State) -> Literal["tools", "__end__"]:
    # Safety guard first: never loop forever.
    if state["iterations"] >= MAX_ITERATIONS:
        return END
    last = state["messages"][-1]
    if getattr(last, "tool_calls", None):
        return "tools"
    return END  # no tool call -> the last message IS the final answer


# ---------- Build ----------

builder = StateGraph(State)
builder.add_node("agent", agent)
builder.add_node("tools", ToolNode(TOOLS))

builder.add_edge(START, "agent")
builder.add_conditional_edges("agent", should_continue, {"tools": "tools", END: END})
builder.add_edge("tools", "agent")

# Checkpointer gives the agent memory across turns.
app = builder.compile(checkpointer=MemorySaver())

if __name__ == "__main__":
    config = {"configurable": {"thread_id": "research-session-1"}}

    print("=== Turn 1: research question ===")
    r1 = app.invoke({"messages": [HumanMessage(content="What is LangGraph?")], "iterations": 0}, config)
    print("Answer:", r1["messages"][-1].content)

    print("\n=== Turn 2: follow-up (same thread, memory!) ===")
    r2 = app.invoke({"messages": [HumanMessage(content="What is 2+2?")], "iterations": 0}, config)
    print("Answer:", r2["messages"][-1].content)

    print("\nTotal messages kept in memory for this thread:", len(r2["messages"]))
