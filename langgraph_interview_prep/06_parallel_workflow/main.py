"""
Project 06 - Parallel Workflow
==============================
Three branches run in the SAME step (in parallel), then an
aggregator combines their results.

LangGraph runs every node whose inputs are ready at the same time.
Here START fans out to weather/hotels/activities, and the aggregator
waits until all three finish.

Graph:
   START
    |
    +---> weather
    |
    +---> hotels    --->  aggregator -> END
    |
    +---> activities

Run:  python main.py
"""

from typing import TypedDict
from langgraph.graph import StateGraph, START, END


class State(TypedDict):
    destination: str
    weather: str
    hotels: str
    activities: str
    summary: str


def weather_node(state: State):
    print(">>> weather (branch 1)")
    return {"weather": f"Sunny, 28C in {state['destination']}"}


def hotels_node(state: State):
    print(">>> hotels (branch 2)")
    return {"hotels": f"3 hotels available in {state['destination']}"}


def activities_node(state: State):
    print(">>> activities (branch 3)")
    return {"activities": f"5 activities in {state['destination']}"}


def aggregator(state: State):
    """Runs only after ALL three branches finish."""
    print(">>> aggregator (after all branches)")
    return {
        "summary": (
            f"{state['weather']}\n{state['hotels']}\n{state['activities']}"
        )
    }


builder = StateGraph(State)
builder.add_node("weather", weather_node)
builder.add_node("hotels", hotels_node)
builder.add_node("activities", activities_node)
builder.add_node("aggregator", aggregator)

# Fan-out: START goes to all three branches at once.
builder.add_edge(START, "weather")
builder.add_edge(START, "hotels")
builder.add_edge(START, "activities")

# Fan-in: each branch leads to the aggregator.
builder.add_edge("weather", "aggregator")
builder.add_edge("hotels", "aggregator")
builder.add_edge("activities", "aggregator")

builder.add_edge("aggregator", END)

app = builder.compile()

if __name__ == "__main__":
    result = app.invoke({"destination": "Goa"})
    print("\nFinal summary:\n" + result["summary"])
