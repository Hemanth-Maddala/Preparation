"""
Project 14 - Planner + Executor (Plan-and-Execute)
==================================================
1) A Planner creates a LIST of steps for a goal.
2) An Executor runs the steps one by one (looping through the plan).
3) A final node combines the results.

This is different from ReAct: the plan is made FIRST, then executed.
ReAct decides the next action one step at a time.

Flow:
   START -> planner -> execute_step <-> (loop) -> final_response -> END

Everything is driven by a REAL LLM - Gemini (key from .env).
No mock LLM, no mock executor, no hardcoded keys.

Setup:
  Copy .env.example to .env and set your key:
    GEMINI_API_KEY=your_gemini_api_key

Run:  python main.py
"""

import os
from typing import Annotated, Literal, TypedDict
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langgraph.graph import StateGraph, START, END
from dotenv import load_dotenv

load_dotenv()  # loads GEMINI_API_KEY from .env (never hardcode keys)

MAX_STEPS = 5


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
    task: str
    plan: list[str]
    index: int
    results: Annotated[list, lambda a, b: a + b]
    final: str


def planner(state: State):
    """Ask the LLM to break the task into numbered steps."""
    print(">>> planner")
    prompt = [
        SystemMessage(content=(
            "You are a planner. Return a plan as numbered steps, "
            "one per line, each step a concrete action.")),
        HumanMessage(content=state["task"]),
    ]
    response = llm.invoke(prompt)
    plan = [l.split(". ", 1)[-1].strip() for l in response.content.splitlines() if l.strip()]
    return {"plan": plan[:MAX_STEPS], "index": 0}


def execute_step(state: State):
    """Ask the LLM to actually DO the current plan step."""
    idx = state["index"]
    step = state["plan"][idx]
    print(f">>> execute step {idx + 1}: {step}")
    prompt = [
        SystemMessage(content=(
            "You are an executor. Complete the given step for the task. "
            "Return a concise, concrete result.")),
        HumanMessage(content=f"Task: {state['task']}\nStep: {step}"),
    ]
    response = llm.invoke(prompt)
    return {"results": [f"Step {idx + 1} ({step}): {response.content.strip()}"], "index": idx + 1}


def more_steps(state: State) -> Literal["execute_step", "final_response"]:
    """Loop control: are there steps left to execute?"""
    if state["index"] < len(state["plan"]):
        return "execute_step"
    return "final_response"


def final_response(state: State):
    print(">>> final response")
    return {"final": "\n".join(state["results"])}


builder = StateGraph(State)
builder.add_node("planner", planner)
builder.add_node("execute_step", execute_step)
builder.add_node("final_response", final_response)

builder.add_edge(START, "planner")
builder.add_edge("planner", "execute_step")
# The loop: execute a step, check if more remain, run the next.
builder.add_conditional_edges("execute_step", more_steps, {"execute_step": "execute_step", "final_response": "final_response"})
builder.add_edge("final_response", END)

app = builder.compile()

if __name__ == "__main__":
    result = app.invoke({"task": "Plan a 3-day trip", "plan": [], "index": 0, "results": [], "final": ""})
    print("\nFINAL PLAN RESULT:\n" + result["final"])
