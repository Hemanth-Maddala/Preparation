"""
Project 17 - Multi-Agent System (Supervisor Pattern)
====================================================
A travel-planning system where MULTIPLE specialized LLM agents
collaborate under a Supervisor, built with LangGraph.

Agents:
  1. RESEARCHER  - gathers useful info about the destination.
  2. PLANNER     - turns research into a day-by-day itinerary.
  3. REVIEWER    - checks the itinerary, finds problems / gaps.
  4. SUPERVISOR  - coordinates: picks the next agent, decides when done.

Architecture:

                    USER
                     |
                     v
                SUPERVISOR  <-------------------+
          +---------+---------+                  |
          |         |         |                  |
          v         v         v                  |
      RESEARCHER PLANNER  REVIEWER               |
          |         |         |                  |
          +----+----+----+----+                  |
                     |                           |
                     v                           |
                SUPERVISOR  --------------------+ (loop until review approves)
                     |
                   finalize
                     |
                    END

Everything uses a REAL LLM - Gemini (key from .env). No mock LLM.

CURRENT LangGraph APIs used:
  - StateGraph / START / END
  - Command(goto=..., update=...) for dynamic supervisor routing
  - Structured output (pydantic) so the supervisor and the reviewer
    return typed decisions instead of fragile free text

Setup:
  Copy .env.example to .env and set GEMINI_API_KEY=your_key
Run:
  python main.py
"""

import os
from typing import Annotated, Literal, TypedDict

from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.graph import StateGraph, START, END
from langgraph.types import Command
from dotenv import load_dotenv
from pydantic import BaseModel, Field

load_dotenv()  # loads GEMINI_API_KEY from .env (never hardcode keys)

MAX_ROUNDS = 8  # safety: cap how many times the supervisor can route


# ---------- Real LLM (Gemini, key from .env) ----------

def get_llm():
    key = os.getenv("GEMINI_API_KEY")
    if not key:
        raise SystemExit(
            "GEMINI_API_KEY not found. Copy .env.example to .env and "
            "set GEMINI_API_KEY=<your key>, then run again."
        )
    from langchain_google_genai import ChatGoogleGenerativeAI
    return ChatGoogleGenerativeAI(
        model=os.getenv("GEMINI_MODEL", "gemini-2.5-flash"),
        api_key=key,
        temperature=0.3,
    )


llm = get_llm()


# ---------- Structured decisions (typed LLM output) ----------

class Route(BaseModel):
    """The supervisor's decision: which single agent should run next."""
    next_agent: Annotated[
        Literal["researcher", "planner", "reviewer", "finalize"],
        Field(description="The agent that should run next. Use 'finalize' only when review_ok is true."),
    ]
    reason: str = Field(default="", description="One short sentence explaining the choice.")


class Review(BaseModel):
    """The reviewer's typed verdict + feedback."""
    verdict: Annotated[
        Literal["APPROVED", "REVISIONS NEEDED"],
        Field(description="APPROVED if the itinerary is good enough to ship, REVISIONS NEEDED otherwise."),
    ]
    feedback: str = Field(description="Specific problems, missing info, and what to fix.")


router = llm.with_structured_output(Route, method="function_calling")
review_llm = llm.with_structured_output(Review, method="function_calling")


# ---------- State ----------

class PlanState(TypedDict):
    request: str                                   # the user's trip request
    research: str                                  # researcher output
    itinerary: str                                 # planner output
    review: str                                    # reviewer feedback text
    review_ok: bool                                # reviewer's typed verdict
    fix_rounds: int                                # planner runs since last review
    final: str                                     # final assembled answer
    next_agent: str                                # last decision (visibility)
    sequence: Annotated[list, lambda a, b: a + b]  # routing history (reducer appends)
    rounds: int                                    # supervisor loop counter (safety)


# ---------- Supervisor Agent ----------

SUPERVISOR_PROMPT = """\
You are the SUPERVISOR of a travel-planning multi-agent team. \
You do NOT plan trips yourself. You pick ONE agent to run next.

Available agents:
- researcher: gathers useful, factual information about the destination.
- planner: creates or improves the day-by-day itinerary using research and review feedback.
- reviewer: critically reviews the itinerary, returns a typed verdict (APPROVED / REVISIONS NEEDED) and feedback.
- finalize: FINISH the task. Use ONLY when review_ok is true.

Follow these rules IN ORDER:
1. If research is empty -> send researcher.
2. If itinerary is empty -> send planner.
3. If there is no review yet -> send reviewer (always review at least once).
4. If review_ok is true -> send finalize.
5. If the itinerary failed review and has NOT been fixed yet (fix_rounds == 0) -> send planner.
6. If the itinerary failed review and the planner ALREADY fixed it (fix_rounds > 0) -> send reviewer to re-check.
7. Never send the same agent twice in a row without a reason.
"""


def _state_summary(state: PlanState) -> str:
    def snip(text: str, n: int = 700) -> str:
        text = text.strip()
        return text if len(text) <= n else text[:n] + " ..."
    return (
        f"User request: {state['request']}\n\n"
        f"[research] {'EMPTY' if not state['research'] else snip(state['research'])}\n\n"
        f"[itinerary] {'EMPTY' if not state['itinerary'] else snip(state['itinerary'])}\n\n"
        f"[review_ok] {state['review_ok']}\n"
        f"[fix_rounds] {state['fix_rounds']}\n\n"
        f"[review feedback] {'EMPTY' if not state['review'] else snip(state['review'])}"
    )


def supervisor(state: PlanState):
    rounds = state["rounds"] + 1
    if rounds > MAX_ROUNDS:
        print(f">>> supervisor (round {rounds}) - max rounds reached, finishing")
        return Command(
            goto="finalize",
            update={"next_agent": "finalize", "sequence": ["finalize"], "rounds": rounds},
        )
    print(f">>> supervisor (round {rounds}) deciding next agent...")
    decision = router.invoke([
        SystemMessage(content=SUPERVISOR_PROMPT),
        HumanMessage(content=_state_summary(state)),
    ])
    print(f"    supervisor -> {decision.next_agent}  ({decision.reason})")
    return Command(
        goto=decision.next_agent,
        update={"next_agent": decision.next_agent, "sequence": [decision.next_agent], "rounds": rounds},
    )


# ---------- Research Agent ----------

def researcher(state: PlanState):
    print(">>> researcher: researching the destination")
    prompt = [
        SystemMessage(content=(
            "You are a travel RESEARCH agent. Think about the destination the "
            "user wants to visit and produce genuinely useful information: "
            "best season, how to get there, local transport, where to stay, "
            "safety, food, and a short list of must-do activities.")),
        HumanMessage(content=state["request"]),
    ]
    response = llm.invoke(prompt)
    return Command(goto="supervisor", update={"research": response.content.strip()})


# ---------- Planner Agent ----------

def planner(state: PlanState):
    print(">>> planner: building the itinerary")
    feedback = state["review"] or "No review feedback yet."
    prompt = [
        SystemMessage(content=(
            "You are a travel PLANNER. Create a realistic, day-by-day itinerary "
            "that matches the user's request (number of days, budget, interests). "
            "Use the research to pick real activities. If review feedback is "
            "provided, fix those specific problems. Be concrete: for each day list "
            "morning / afternoon / evening plans.")),
        HumanMessage(content=(
            f"Request: {state['request']}\n\n"
            f"Research:\n{state['research']}\n\n"
            f"Previous review feedback (fix this):\n{feedback}")),
    ]
    response = llm.invoke(prompt)
    return Command(
        goto="supervisor",
        update={"itinerary": response.content.strip(), "fix_rounds": state["fix_rounds"] + 1},
    )


# ---------- Reviewer Agent ----------

def reviewer(state: PlanState):
    print(">>> reviewer: reviewing the itinerary")
    review = review_llm.invoke([
        SystemMessage(content=(
            "You are a travel REVIEWER. Scrutinize the itinerary for problems: "
            "unrealistic timings, missing days, ignored budget, skipped research "
            "suggestions, missing transport/accommodation/food details. "
            "Return your verdict and specific feedback.")),
        HumanMessage(content=(
            f"Request: {state['request']}\n\n"
            f"Research:\n{state['research']}\n\n"
            f"Itinerary:\n{state['itinerary']}")),
    ])
    return Command(
        goto="supervisor",
        update={
            "review": review.feedback.strip(),
            "review_ok": review.verdict == "APPROVED",
            "fix_rounds": 0,  # fresh review -> any future fix starts from zero
        },
    )


# ---------- Finalize ----------

def finalize(state: PlanState):
    print(">>> finalize: assembling the answer")
    verdict = "APPROVED" if state["review_ok"] else "COMPLETE (with review notes)"
    final = (
        f"=== FINAL TRIP PLAN ===\n\n"
        f"Request: {state['request']}\n\n"
        f"--- ITINERARY ---\n{state['itinerary']}\n\n"
        f"--- RESEARCH (why it works) ---\n{state['research']}\n\n"
        f"--- REVIEW ---\n{state['review']}\n\n"
        f"Status: {verdict}"
    )
    return Command(goto=END, update={"final": final})


# ---------- Build the graph ----------

builder = StateGraph(PlanState)
builder.add_node("supervisor", supervisor)
builder.add_node("researcher", researcher)
builder.add_node("planner", planner)
builder.add_node("reviewer", reviewer)
builder.add_node("finalize", finalize)

builder.add_edge(START, "supervisor")
# All further routing happens dynamically via Command(goto=...).

app = builder.compile()

if __name__ == "__main__":
    request = input("Enter your trip request (default: 'Plan a 3-day trip to Goa.'): ").strip()
    if not request:
        request = "Plan a 3-day trip to Goa."

    result = app.invoke(
        {
            "request": request,
            "research": "",
            "itinerary": "",
            "review": "",
            "review_ok": False,
            "fix_rounds": 0,
            "final": "",
            "next_agent": "",
            "sequence": [],
            "rounds": 0,
        },
        config={"recursion_limit": 50},
    )
    print("\n" + "=" * 60)
    print(result["final"])
    print("=" * 60)
    print(f"\nRouting sequence: {' -> '.join(result['sequence'])}")
    print(f"Supervisor rounds: {result['rounds']}")
