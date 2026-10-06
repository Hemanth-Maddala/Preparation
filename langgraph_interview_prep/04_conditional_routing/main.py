"""
Project 04 - Conditional Routing
================================
Branch a request to one of three nodes based on a routing function.

Graph:
   START -> classify -> (travel | food | other) -> END

The routing function is a plain Python function that returns
a STRING. LangGraph uses that string as a key in a mapping
{ "travel": "travel_node", "food": "food_node", ... }
to pick the next node.

Run:  python main.py
"""

from typing import TypedDict, Literal
from langgraph.graph import StateGraph, START, END


class State(TypedDict):
    request: str
    category: str
    answer: str


def classify(state: State):
    """A mock classifier. In a real app an LLM or model does this."""
    print(">>> classify")
    text = state["request"].lower()
    if any(w in text for w in ["restaurant", "pizza", "food"]):
        category = "food"
    elif any(w in text for w in ["trip", "flight", "hotel", "goa"]):
        category = "travel"
    else:
        category = "other"
    return {"category": category}


def handle_travel(state: State):
    print(">>> travel node")
    return {"answer": f"Travel help: best flights to {state['request']}"}


def handle_food(state: State):
    print(">>> food node")
    return {"answer": f"Food help: here are restaurants for {state['request']}"}


def handle_general(state: State):
    print(">>> other node")
    return {"answer": f"General help about: {state['request']}"}


def route_after_classify(state: State) -> Literal["travel", "food", "other"]:
    """The routing function. Returns a STRING that is used as a KEY
    in the path map to pick the next node."""
    return state["category"]


builder = StateGraph(State)
builder.add_node("classify", classify)
builder.add_node("travel_node", handle_travel)
builder.add_node("food_node", handle_food)
builder.add_node("other_node", handle_general)

builder.add_edge(START, "classify")

# Conditional edge: after classify, the routing function decides
# which node runs next. The dict maps routing value -> node name.
builder.add_conditional_edges(
    "classify",
    route_after_classify,
    {
        "travel": "travel_node",
        "food": "food_node",
        "other": "other_node",
    },
)

builder.add_edge("travel_node", END)
builder.add_edge("food_node", END)
builder.add_edge("other_node", END)

app = builder.compile()

if __name__ == "__main__":
    for request in ["Plan a trip to Goa", "Find a pizza place", "Tell me a joke"]:
        result = app.invoke({"request": request})
        print(f"\nRequest: {request!r}\nCategory: {result['category']}\nAnswer: {result['answer']}")
