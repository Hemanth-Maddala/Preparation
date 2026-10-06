# Project 16 - Autonomous Goal-Directed Agent

## 1. What this project teaches
How to build a small autonomous agent that pursues a GOAL by deciding its own actions, observing results, and knowing when it is done.

## 2. Problem statement
User gives a goal: "Find the best option from these products under ₹80,000 and recommend one." The agent must gather data (search catalog, compare products) and produce a recommendation - without any hard-coded step order.

## 3. LangGraph concepts being demonstrated
- Goal-directed behavior
- The agent loop (decide -> act -> observe -> decide)
- ReAct as the engine of the loop
- Re-planning (every turn re-decides based on new observations)
- Tool use constrained to a defined set
- State tracking (goal, messages, steps)
- Goal-completion detection (no more tool calls = done)
- Safety constraints (max iterations)
- Autonomy: the AGENT decides the next action, not the graph

## 4. Simple architecture / graph diagram

```
            GOAL
              |
              v
     decide_next_action  <----------+
         |      \                    |
  (tool_call?)  (final answer)      |
     |                |             |
     v                v             |
   tools       capture_final_answer |
     |                |             |
     +----------------+-------------+
                       |
                       v
                      END
```

NOT hard-coded A->B->C: the only fixed thing is the loop. Which tool runs and how many turns happen is decided at runtime.

## 5. Step-by-step execution flow
1. The goal is stored in state.
2. `decide_next_action` asks Gemini: "what next?" It decides to search the catalog.
3. `tools` runs `search_products`; the observation goes into messages.
4. Loop back. `decide_next_action` now sees the catalog -> decides to compare.
5. `tools` runs `compare_products`; observation added.
6. Loop back. Gemini sees a winner -> produces a final answer (no tool call).
7. Routing detects "no tool call" -> goal complete -> capture answer -> END.

(The number of turns is decided at runtime by the model - this is the autonomy.)

## 6. Important code explanation
- **The agent, not the graph, chooses the next action.** The graph only provides the loop + tools. Decisions come from Gemini reading observations.
- `should_continue` = the goal-completion check + infinite-loop safety net.
- Tool results accumulate in `messages` via `add_messages`; that IS the agent's memory of what it has done.
- The LLM is real Gemini (key from `.env` via `load_dotenv`) - no mock decisions.

## 7. Expected output
(Real Gemini - the exact tool sequence may vary; here is a likely one.)
```
[llm] Using Gemini
>>> deciding action (step 1)
>>> deciding action (step 2)
>>> deciding action (step 3)

STEPS TAKEN: 3

FINAL ANSWER:
FINAL ANSWER: I compared Phone X and Phone Y. I recommend Phone Y ...

Full action history (decisions + observations):
  HumanMessage: Goal: Find the best option ...
  AIMessage:  (tool call)
  ToolMessage: Found products under 80000: ...
  AIMessage:  (tool call)
  ToolMessage: Winner: Phone Y ...
  AIMessage: FINAL ANSWER: ...
```

## 8. What I should remember for an interview (IMPORTANT)
- **What is an autonomous agent?** A system that pursues a goal by deciding its own sequence of actions, observing results, and re-deciding - within constraints.
- **Is ReAct the same as an autonomous agent?** NO. ReAct is a reasoning PATTERN (Reason -> Act -> Observe -> Repeat). An autonomous agent is a broader BEHAVIOR/system that pursues a goal; it can USE a ReAct loop as its engine. This project uses a ReAct loop to make the agent autonomous. They are related, not separate technologies.
- **What makes an agent autonomous?** It chooses the next action at runtime based on observations/state, instead of following a fixed script.
- **How do you prevent infinite loops?** A max-iterations counter in state, checked before continuing.
- **How do you constrain an agent?** A fixed tool set, a schema for each tool, iteration limits, and validation/approval layers.
- **How do you know the goal is complete?** The model stops requesting tools and produces a final answer; the routing function detects this. (You can also add explicit "done" signals or a verifier.)
- **What if the agent chooses the wrong tool?** Add error handling: tool exceptions become ToolMessages, the agent observes the failure and re-plans. Also cap retries.
- **How to add human approval?** Insert `interrupt()` before risky actions (Project 10 pattern) so a human approves before the tool runs.

## 9. Possible interviewer questions
- What is an autonomous agent?
- Is ReAct the same as an autonomous agent?
- How does ReAct relate to autonomy?
- What makes an agent autonomous?
- How would you implement an autonomous loop in LangGraph?
- How do you prevent an autonomous agent from running forever?
- How do you know when the goal is complete?
- What happens if the agent chooses the wrong tool?
- How would you add human approval?

## 10. "Can I write this from memory?" checklist
- [ ] I can build a goal-loop (decide -> tools -> decide)
- [ ] I can make the agent choose tools at runtime
- [ ] I can detect goal completion (no tool calls -> answer)
- [ ] I can add a max-iterations safety guard
- [ ] I can explain ReAct vs autonomous agent correctly
- [ ] I can explain how to constrain an agent
