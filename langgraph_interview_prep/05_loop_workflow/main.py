"""
Project 05 - Loop / Iterative Workflow
======================================
A cycle in LangGraph. Generate an answer, evaluate it,
and if it is not good enough, improve it and loop back.

Cycles are just a conditional edge that points BACK to a node.

Run:  python main.py
"""

from typing import TypedDict, Literal
from langgraph.graph import StateGraph, START, END

MAX_ITERATIONS = 3


class State(TypedDict):
    topic: str
    answer: str
    iteration: int
    evaluation: str


def generate_answer(state: State):
    print(f">>> generate (iteration {state['iteration']})")
    # Mock: answer quality improves with each loop pass.
    quality = state["iteration"]
    return {
        "answer": f"{'Good' * (quality + 1)} answer about {state['topic']}.",
    }


def evaluate_answer(state: State):
    """A real node that decides whether the answer is good enough."""
    print(">>> evaluate: is it good enough?")
    # Good enough when we hit the iteration limit (mock quality check).
    evaluation = "good" if state["iteration"] >= MAX_ITERATIONS else "improve"
    return {"evaluation": evaluation}


def route_after_evaluate(state: State) -> Literal["improve_answer", "__end__"]:
    """The routing function reads the evaluation and decides the next node."""
    return "good" if state["evaluation"] == "good" else "improve"


def improve_answer(state: State):
    print(f">>> improve (iteration {state['iteration']})")
    # Write the improved answer AND bump the counter.
    return {
        "answer": state["answer"] + " (improved)",
        "iteration": state["iteration"] + 1,
    }


builder = StateGraph(State)
builder.add_node("generate_answer", generate_answer)
builder.add_node("evaluate_answer", evaluate_answer)
builder.add_node("improve_answer", improve_answer)

builder.add_edge(START, "generate_answer")
builder.add_edge("generate_answer", "evaluate_answer")

# The loop: improve -> generate -> evaluate -> improve -> ...
builder.add_conditional_edges(
    "evaluate_answer",
    route_after_evaluate,
    {"improve": "improve_answer", "good": END},
)
builder.add_edge("improve_answer", "generate_answer")

app = builder.compile()

if __name__ == "__main__":
    result = app.invoke({"topic": "LangGraph", "answer": "", "iteration": 0, "evaluation": ""})
    print("\nFinal answer:", result["answer"])
    print("Iterations used:", result["iteration"])
