"""
Project 13 - Command / Dynamic Control Flow
===========================================
Command lets a NODE both update state AND choose the next node
in one return. This is the current LangGraph API for dynamic
control flow.

Flow:
   START -> analyze -> (book | cancel | info) -> execute -> END

The `analyze` node returns Command(goto=<chosen node>, update={...}).

Compare with project 04: conditional edges = the NEXT node is chosen
by an edge function; Command = the NODE itself chooses and can update
state at the same time.

Run:  python main.py
"""

from typing import Literal, TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.types import Command


class State(TypedDict):
    request: str
    action: str
    result: str


def analyze(state: State) -> Command[Literal["book_node", "cancel_node", "info_node"]]:
    """A node that DECIDES what happens next."""
    text = state["request"].lower()

    if "cancel" in text:
        # goto = next node, update = state change, in ONE return.
        return Command(goto="cancel_node", update={"action": "cancel"})
    if "book" in text:
        return Command(goto="book_node", update={"action": "book"})
    return Command(goto="info_node", update={"action": "info"})


def book_node(state: State):
    print(">>> book")
    return {"result": "Booking confirmed."}


def cancel_node(state: State):
    print(">>> cancel")
    return {"result": "Booking cancelled."}


def info_node(state: State):
    print(">>> info")
    return {"result": "Here is the flight information."}


def execute(state: State):
    print(">>> execute")
    return {"result": f"Executed: {state['result']}"}


builder = StateGraph(State)
builder.add_node("analyze", analyze)
builder.add_node("book_node", book_node)
builder.add_node("cancel_node", cancel_node)
builder.add_node("info_node", info_node)
builder.add_node("execute", execute)

builder.add_edge(START, "analyze")

# The routing target is chosen by the node itself (no add_conditional_edges).
builder.add_edge("book_node", "execute")
builder.add_edge("cancel_node", "execute")
builder.add_edge("info_node", "execute")

builder.add_edge("execute", END)

app = builder.compile()

if __name__ == "__main__":
    for request in ["book a flight", "cancel my booking", "show flight info"]:
        result = app.invoke({"request": request})
        print(f"\nRequest: {request!r}\nAction: {result['action']}\nResult: {result['result']}")
