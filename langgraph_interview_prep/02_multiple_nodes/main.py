"""
Project 02 - Multiple Nodes
===========================
Three nodes in a chain. Each node reads the state, changes it,
and passes it forward.

Graph:  START -> preprocess -> process -> format -> END

Run:  python main.py
"""

from typing import TypedDict
from langgraph.graph import StateGraph, START, END


class State(TypedDict):
    raw: str
    cleaned: str
    count: int
    output: str


def preprocess(state: State):
    print(f"1. preprocess  | raw={state['raw']!r}")
    cleaned = state["raw"].strip().lower()
    return {"cleaned": cleaned}


def process(state: State):
    print(f"2. process     | cleaned={state['cleaned']!r}")
    words = state["cleaned"].split()
    return {"count": len(words)}


def format_output(state: State):
    print(f"3. format      | count={state['count']}")
    return {"output": f"{state['count']} words"}


builder = StateGraph(State)
builder.add_node("preprocess", preprocess)
builder.add_node("process", process)
builder.add_node("format_output", format_output)

# Chain: START -> preprocess -> process -> format_output -> END
builder.add_edge(START, "preprocess")
builder.add_edge("preprocess", "process")
builder.add_edge("process", "format_output")
builder.add_edge("format_output", END)

app = builder.compile()

if __name__ == "__main__":
    result = app.invoke({"raw": "  Hello LangGraph World  "})
    print("\nFinal state:", result)
