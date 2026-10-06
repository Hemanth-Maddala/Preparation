# Project 17 - Multi-Agent System (Supervisor Pattern)

## 1. What this project teaches
How to build a MULTI-AGENT system in LangGraph: multiple specialized LLM agents that collaborate, coordinated by a central SUPERVISOR that routes work and decides when the task is complete.

## 2. Problem statement
User gives: "Plan a 3-day trip to Goa." Four agents cooperate:
1. **Research Agent** - gathers useful info about the destination (season, transport, stay, food, activities).
2. **Planner Agent** - turns the research into a day-by-day itinerary.
3. **Reviewer Agent** - reviews the itinerary, finds problems / missing info, suggests fixes.
4. **Supervisor Agent** - coordinates the others, decides which agent runs next and when the task is done.

## 3. LangGraph concepts being demonstrated
- Multi-agent supervisor architecture
- `Command(goto=..., update=...)` for dynamic routing (the CURRENT LangGraph API)
- Structured output (pydantic `BaseModel`) so the supervisor picks exactly one agent
- Shared state between agents (research / itinerary / review fields)
- A routing loop: supervisor -> agent -> supervisor -> ... until FINISH
- Loop safety: `MAX_ROUNDS` cap + `recursion_limit`
- Real LLM (Gemini) with the key loaded from `.env` - **no mock LLM, no hardcoded keys**

## 4. Simple architecture / graph diagram

```
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
```

## 5. Step-by-step execution flow
1. `supervisor` reads the state. Research is empty -> routes to `researcher`.
2. `researcher` produces destination info, then `Command(goto="supervisor")` returns control.
3. `supervisor` sees an itinerary is missing -> routes to `planner`.
4. `planner` builds the itinerary (increments `fix_rounds`), returns to `supervisor`.
5. `supervisor` sees the itinerary was never reviewed -> routes to `reviewer`.
6. `reviewer` returns a TYPED verdict (`APPROVED` / `REVISIONS NEEDED`) + feedback, writes `review_ok`, resets `fix_rounds`, returns to `supervisor`.
7. `supervisor` reads `review_ok`:
   - not approved & not yet fixed (`fix_rounds == 0`) -> `planner` (fix the feedback).
   - already fixed (`fix_rounds > 0`) -> `reviewer` again (re-check).
   - approved -> `finalize`.
8. `finalize` assembles the final answer and ends the graph.

## 6. Important code explanation
- `class Route(BaseModel)` + `llm.with_structured_output(Route, method="function_calling")` forces the supervisor to answer with valid JSON: `{"next_agent": "...", "reason": "..."}`.
- The reviewer ALSO uses structured output (`class Review`): a typed `verdict` + `feedback`. No fragile text parsing; `review_ok = (verdict == "APPROVED")` is a boolean in state.
- `Command(goto="supervisor", update={...})` - a worker node tells LangGraph "run supervisor next" and writes its output into the shared state.
- `fix_rounds` breaks a subtle loop: after the planner fixes the itinerary, the supervisor must route to the REVIEWER again (not straight back to planner). Rule: `fix_rounds == 0` -> planner; `fix_rounds > 0` -> reviewer.
- `sequence: Annotated[list, lambda a, b: a + b]` accumulates the routing history; the reducer makes the list append instead of overwrite.
- `MAX_ROUNDS` in the supervisor + `recursion_limit` in `invoke` are the two safety nets against an infinite agent loop.

## 7. Setup & run
```
pip install -r requirements.txt
copy .env.example .env     # then put your real GEMINI_API_KEY in .env
python main.py
```
Expected output shape: a log of the routing decisions (`supervisor -> researcher`, etc.), then a `FINAL TRIP PLAN` with the itinerary, research, review, and the routing sequence.

## 8. What I should remember for an interview
- **Why multi-agent?** Complex tasks decompose into specialized agents; each has a narrow, high-quality focus; the supervisor allocates work dynamically.
- **Supervisor pattern vs pipeline?** A pipeline always runs A -> B -> C. A supervisor DECIDES at runtime which agent runs next based on state - the path is not fixed.
- **How do agents communicate?** Through the SHARED state. Each agent reads what previous agents wrote and writes its own output, then returns to the supervisor.
- **How does the supervisor know when to stop?** It reads the state (here: the reviewer's verdict). "Stop condition" is the reviewer approving; the safety caps are a backstop.
- **What is `Command`?** A LangGraph object a node returns to dynamically control routing (`goto`) and update state (`update`). It replaces hardcoded conditional edges for supervisor patterns.
- **What is structured output?** Constraining the LLM to reply in a fixed schema (via function calling) so you get a typed decision you can route on - no fragile string parsing.
- **How do you prevent infinite agent loops?** A round/iteration counter in state, a max limit, and `recursion_limit` on invoke.

## 9. Possible interviewer questions
- Why would you use multiple agents instead of one?
- Explain the supervisor architecture. Who decides the next agent?
- How do agents pass information to each other?
- How does the supervisor decide the task is complete?
- What is Command and how does it route in LangGraph?
- Why structured output for the supervisor decision?
- How do you stop a multi-agent loop from running forever?
- What are the failure modes of a multi-agent system? (Context/token growth, loops, cost, a weak reviewer always approving.)

## 10. "Can I write this from memory?" checklist
- [ ] I can define a Route schema and structured output
- [ ] I can write a supervisor node returning Command(goto=...)
- [ ] I can make workers return Command(goto="supervisor")
- [ ] I can use structured output for the reviewer verdict too
- [ ] I can wire shared state between agents
- [ ] I can explain the stop condition, the fix/re-review loop, and loop safety
- [ ] I can explain supervisor vs pipeline vs swarm
