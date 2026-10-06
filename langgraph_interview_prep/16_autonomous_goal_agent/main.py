"""
Project 16 - Autonomous Goal-Directed Agent
===========================================
The agent is given a GOAL and must decide its OWN actions to
complete it. Nothing is hard-coded like Node A -> Node B -> Node C.

Instead: the agent loops on 3 questions until the goal is met:
   1. What do I know? (state / observations)
   2. What action should I take next? (choose a tool, or answer)
   3. Is the goal complete? (no more tool calls -> final answer)

The ONLY structure is a loop:
   decide -> act (tool) -> observe -> decide -> ...

This loop is the same ReAct pattern, used as the engine of an
autonomous agent. Constraints keep it safe: a fixed set of tools,
a max-iterations guard, and state that records everything.

The LLM is REAL - Gemini, with the key loaded from .env
(no hardcoded keys, no mock decisions).

Goal example: "Find the best option from these products under
Rs. 80,000 and recommend one."

Setup:
  Copy .env.example to .env and set your key:
    GEMINI_API_KEY=your_gemini_api_key

Run:  python main.py
"""

import os
from typing import Annotated, Literal, TypedDict
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage, SystemMessage
from langchain_core.tools import tool
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode
from dotenv import load_dotenv

load_dotenv()  # loads GEMINI_API_KEY from .env (never hardcode keys)

MAX_ITERATIONS = 5


# ---------- The agent's allowed tools (its "action space") ----------

@tool
def search_products(budget: int) -> str:
    """Search mock catalog for products under the budget."""
    return ("Found products under 80000:\n"
            "- Phone X: 55000, 6.1 inch, 128GB\n"
            "- Phone Y: 75000, 6.7 inch, 256GB, better camera\n"
            "- Tablet Z: 45000, 10 inch")


@tool
def compare_products(product_a: str, product_b: str) -> str:
    """Compare two products and declare a winner."""
    if "Y" in product_a:
        return f"Winner: {product_a} (better camera, more storage)"
    return f"Winner: {product_b}"


TOOLS = [search_products, compare_products]


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
    system = SystemMessage(content=(
        "You are an autonomous agent. You must pursue the user's goal. "
        "Decide the next action: call a tool to gather data, or when you "
        "have enough data give a final answer that begins with FINAL ANSWER."))
    return ChatGoogleGenerativeAI(
        model=os.getenv("GEMINI_MODEL", "gemini-2.5-flash"),
        api_key=key,
        temperature=0,
    ).bind_tools(TOOLS)


llm = get_llm()


# ---------- State: goal + full history + progress ----------

class State(TypedDict):
    goal: str
    messages: Annotated[list, add_messages]
    steps_taken: int
    final_answer: str


# ---------- Nodes ----------

def decide_next_action(state: State):
    """The agent's reasoning step: look at state/observations and
    decide the next action. Returns either a tool_call or the final answer."""
    print(f">>> deciding action (step {state['steps_taken'] + 1})")
    prompt = [HumanMessage(content=f"Goal: {state['goal']}")]
    response = llm.invoke(prompt + state["messages"])
    return {"messages": [response], "steps_taken": state["steps_taken"] + 1}


def should_continue(state: State) -> Literal["tools", "__end__"]:
    """Goal-complete check: if the agent stopped requesting tools,
    it has produced the final answer. The iteration cap is a safety net."""
    if state["steps_taken"] >= MAX_ITERATIONS:
        return END  # safety: never run forever
    last = state["messages"][-1]
    if getattr(last, "tool_calls", None):
        return "tools"   # still working toward the goal
    return END           # goal complete -> final answer produced


def capture_final_answer(state: State):
    final = state["messages"][-1].content
    return {"final_answer": final}


# ---------- Build ----------

builder = StateGraph(State)
builder.add_node("decide_next_action", decide_next_action)
builder.add_node("tools", ToolNode(TOOLS))
builder.add_node("capture_final_answer", capture_final_answer)

builder.add_edge(START, "decide_next_action")
builder.add_conditional_edges(
    "decide_next_action", should_continue, {"tools": "tools", END: "capture_final_answer"})
builder.add_edge("tools", "decide_next_action")
builder.add_edge("capture_final_answer", END)

app = builder.compile()

if __name__ == "__main__":
    goal = "Find the best option from these products under 80000 and recommend one."
    result = app.invoke({"goal": goal, "messages": [], "steps_taken": 0, "final_answer": ""})
    print("\nSTEPS TAKEN:", result["steps_taken"])
    print("\nFINAL ANSWER:\n" + result["final_answer"])
    print("\nFull action history (decisions + observations):")
    for m in result["messages"]:
        print(f"  {type(m).__name__}: {m.content or '(tool call)'}")
