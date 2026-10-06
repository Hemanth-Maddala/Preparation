"""
Project 10 - Human in the Loop
==============================
A mocked bank transfer that REQUIRES human approval before execution.

How it works:
  - A node calls interrupt(...) -> the graph PAUSES and returns control.
  - The rest of the graph is NOT executed yet.
  - We call app.invoke(Command(resume="yes"/"no"), config) to resume.
  - The interrupt() call returns the resume value, and execution continues.

interrupt() requires a checkpointer (state must be saved to pause).

Run:  python main.py
"""

from typing import Annotated, Literal, TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.types import Command, interrupt
from langgraph.checkpoint.memory import MemorySaver


class State(TypedDict):
    amount: float
    account: str
    log: Annotated[list, lambda a, b: a + b]  # append-only log
    status: str


def validate(state: State):
    print(">>> validate transaction")
    if state["amount"] <= 0:
        return {"status": "rejected: invalid amount", "log": ["invalid amount"]}
    return {"log": ["validated"]}


def prepare_transaction(state: State):
    print(">>> prepare transaction")
    return {
        "log": [f"prepared transfer of {state['amount']} to {state['account']}"],
        "status": "pending approval",
    }


def request_human_approval(state: State) -> Command[Literal["execute", "__end__"]]:
    # PAUSE point. Returns control to the caller with this question.
    decision = interrupt({"question": f"Approve transfer of {state['amount']}?"})

    if decision == "yes":
        return Command(goto="execute", update={"status": "approved"})
    return Command(goto=END, update={"status": "rejected by user"})


def execute(state: State):
    print(">>> execute (mock transfer)")
    return {"log": ["executed (mock)"], "status": "executed"}


builder = StateGraph(State)
builder.add_node("validate", validate)
builder.add_node("prepare", prepare_transaction)
builder.add_node("approval", request_human_approval)
builder.add_node("execute", execute)

builder.add_edge(START, "validate")
builder.add_edge("validate", "prepare")
builder.add_edge("prepare", "approval")
builder.add_edge("execute", END)

# Checkpointer is REQUIRED for interrupt/resume to work.
app = builder.compile(checkpointer=MemorySaver())

if __name__ == "__main__":
    config = {"configurable": {"thread_id": "txn-1001"}}

    # 1. First invoke: graph runs until it hits interrupt() and pauses.
    state = app.invoke({"amount": 10000, "account": "Savings-123", "log": [], "status": ""}, config)
    print("\n[paused] status:", state["status"])
    print("[waiting for human decision...]\n")

    # 2. Human approves -> resume the paused graph.
    state = app.invoke(Command(resume="yes"), config)
    print("\n[resumed] status:", state["status"])
    print("log:", state["log"])
