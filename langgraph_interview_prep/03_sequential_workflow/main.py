"""
Project 03 - Sequential Workflow
================================
A realistic but simple travel itinerary pipeline.
Each node does one job and passes its result to the next node.

Graph:
   START -> extract_destination -> generate_activities
        -> generate_itinerary -> final_response -> END

Run:  python main.py
"""

from typing import TypedDict
from langgraph.graph import StateGraph, START, END

# A small mock "knowledge base" used instead of an LLM so this runs offline.
ACTIVITIES = {
    "paris": "Louvre, Eiffel Tower, Seine cruise",
    "goa": "Baga beach, church tour, water sports",
    "tokyo": "Senso-ji, Shibuya, sushi dinner",
}


class State(TypedDict):
    request: str
    destination: str
    activities: str
    itinerary: str
    response: str


def extract_destination(state: State):
    """Find the destination name inside the request text."""
    print("1. extracting destination")
    text = state["request"].lower()
    for place in ACTIVITIES:
        if place in text:
            return {"destination": place}
    return {"destination": "unknown"}


def generate_activities(state: State):
    """Look up activities for the destination."""
    print("2. generating activities")
    return {"activities": ACTIVITIES.get(state["destination"], "city walk")}


def generate_itinerary(state: State):
    """Combine destination + activities into a day plan."""
    print("3. generating itinerary")
    itinerary = (
        f"Day 1 in {state['destination'].title()}: "
        f"{state['activities']}."
    )
    return {"itinerary": itinerary}


def final_response(state: State):
    """Produce the final user-facing message."""
    print("4. writing final response")
    return {"response": f"Here is your plan:\n{state['itinerary']}"}


builder = StateGraph(State)
builder.add_node("extract_destination", extract_destination)
builder.add_node("generate_activities", generate_activities)
builder.add_node("generate_itinerary", generate_itinerary)
builder.add_node("final_response", final_response)

builder.add_edge(START, "extract_destination")
builder.add_edge("extract_destination", "generate_activities")
builder.add_edge("generate_activities", "generate_itinerary")
builder.add_edge("generate_itinerary", "final_response")
builder.add_edge("final_response", END)

app = builder.compile()

if __name__ == "__main__":
    result = app.invoke({"request": "Plan a trip to Paris for 3 days"})
    print("\n" + result["response"])
