"""
Project 09 - Memory / Checkpointing
===================================
A conversational assistant that remembers facts across turns.

Key idea: without a checkpointer, the graph starts fresh on every
invoke. With a checkpointer + thread_id, the full state (including
the message history) is SAVED after every superstep and restored
on the next invoke of the same thread.

Demo:
  Turn 1: "My name is Hemanth."  -> assistant remembers
  Turn 2: "What is my name?"     -> answers correctly

The LLM is REAL - Gemini, with the key loaded from .env
(no hardcoded keys, no mock).

Setup:
  Copy .env.example to .env and set your key:
    GEMINI_API_KEY=your_gemini_api_key

Run:  python main.py
"""

import os
from typing import Annotated, TypedDict
from langchain_core.messages import HumanMessage, AIMessage
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import MemorySaver  # in-memory checkpointer
from dotenv import load_dotenv

load_dotenv()  # loads GEMINI_API_KEY from .env (never hardcode keys)


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
    )


llm = get_llm()


class State(TypedDict):
    messages: Annotated[list, add_messages]  # history grows across turns


def assistant(state: State):
    response = llm.invoke(state["messages"])
    return {"messages": [response]}


builder = StateGraph(State)
builder.add_node("assistant", assistant)
builder.add_edge(START, "assistant")
builder.add_edge("assistant", END)

# THE important line: compile with a checkpointer to persist state.
app = builder.compile(checkpointer=MemorySaver())

if __name__ == "__main__":
    # thread_id = the conversation id. Same thread = same memory.
    config = {"configurable": {"thread_id": "user-hemanth"}}

    print("--- Turn 1 ---")
    r1 = app.invoke({"messages": [HumanMessage(content="My name is Hemanth.")]}, config)

    print("--- Turn 2 (new invoke, same thread) ---")
    r2 = app.invoke({"messages": [HumanMessage(content="What is my name?")]}, config)

    print("\nTurn 2 answer:", r2["messages"][-1].content)
    print("\nFull persisted history for this thread:")
    for m in r2["messages"]:
        print(f"  {type(m).__name__}: {m.content}")
