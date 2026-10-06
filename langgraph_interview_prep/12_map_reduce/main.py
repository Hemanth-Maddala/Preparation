"""
Project 12 - Map Reduce / Send
==============================
Dynamic fan-out: for a LIST of items (unknown at build time), spawn
one parallel "map" run per item, then "reduce" all results together.

Send(node_name, payload) tells LangGraph: run `node_name` in parallel
with `payload` as its input.

Graph:
   START -> map_cities (returns [Send]) -> process_city (x N, in parallel)
        -> aggregate -> END

Run:  python main.py
"""

from typing import Annotated, TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.types import Send


class State(TypedDict):
    cities: list[str]
    results: Annotated[list, lambda a, b: a + b]  # reducer: append
    summary: str


def map_cities(state: State):
    """Return a list of Send objects -> one parallel task per city."""
    return [Send("process_city", {"city": city}) for city in state["cities"]]


def process_city(state: dict):
    """Runs once PER city, in parallel. state here is the Send payload."""
    print(f"  processing {state['city']}")
    return {"results": [f"{state['city']}: 2 days recommended"]}


def aggregate(state: State):
    print("aggregating all results")
    return {"summary": " | ".join(state["results"])}


builder = StateGraph(State)
builder.add_node("process_city", process_city)
builder.add_node("aggregate", aggregate)

# START fans out dynamically: the conditional edge returns Send objects.
builder.add_conditional_edges(START, map_cities, ["process_city"])

builder.add_edge("process_city", "aggregate")
builder.add_edge("aggregate", END)

app = builder.compile()

if __name__ == "__main__":
    result = app.invoke({"cities": ["Delhi", "Goa", "Mumbai"], "results": []})
    print("\nSummary:", result["summary"])
    print("Results:", result["results"])
