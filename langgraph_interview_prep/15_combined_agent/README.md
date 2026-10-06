# Project 15 - Combined Agent (AI Research Assistant)

## 1. What this project teaches
How to combine ALL core LangGraph concepts into one small, real agent.

## 2. Problem statement
An AI research assistant that answers questions, uses tools (search + calculator) when needed, remembers a conversation, and can never loop forever.

## 3. LangGraph concepts being demonstrated (combined)
- State (messages + iteration counter)
- Nodes and edges
- Conditional routing (tool loop vs stop)
- Tools + ToolNode
- ReAct loop (reason -> act -> observe)
- Memory / checkpointing (`MemorySaver` + `thread_id`)
- Loop safety (max iterations)
- Final response from the last AIMessage

## 4. Simple architecture / graph diagram

```
 START -> agent <---------+
            |              |
   (tool_calls? / limit?)  |
      /      \             |
   tools     END  (final   |
      |        answer)     |
      +--------------------+
```

## 5. Step-by-step execution flow
1. Turn 1: user asks "What is LangGraph?" -> `agent` calls the real LLM (Gemini).
2. Gemini decides it needs data -> emits a tool_call to `search_knowledge`.
3. `tools` runs it; ToolMessage is appended; control loops to `agent`.
4. `agent` now sees the observation and produces the final answer (no tool_call) -> END.
5. State (whole conversation) is checkpointed.
6. Turn 2 on the SAME thread_id restores history - the agent has memory.
7. The `iterations` counter guarantees the loop stops at `MAX_ITERATIONS` even with a misbehaving model.

## 6. Important code explanation
- `State` mixes a messages reducer with a plain counter field.
- `should_continue` checks the counter FIRST (safety), then tool_calls.
- `add_messages` + `MemorySaver` + `thread_id` = conversation memory.
- Same loop shape as Project 08, plus memory and a safety cap.
- LLM is real Gemini, key loaded from `.env` via `load_dotenv()` - no mock.

## 7. Expected output
(Real Gemini - exact wording varies, the tool-use shape stays the same.)
```
[llm] Using Gemini
=== Turn 1: research question ===
>>> agent (iteration 1)
>>> agent (iteration 2)
Answer: LangGraph is a library for building stateful LLM agents as graphs.

=== Turn 2: follow-up (same thread, memory!) ===
>>> agent (iteration 1)
>>> agent (iteration 2)
Answer: 4

Total messages kept in memory for this thread: 4
```

## 8. What I should remember for an interview
- A production-ish agent is mostly: a ReAct loop + tools + memory + guards.
- Memory comes from the checkpointer; messages accumulate via `add_messages`.
- Always include a max-iterations guard when the loop is LLM-driven.
- "Final response" = the AIMessage with no tool_calls that routes to END.

## 9. Possible interviewer questions
- How do you combine tools, routing, and memory in one agent?
- How do you prevent an agent from looping forever?
- How do you give an agent multi-turn memory?
- What makes this an agent and not just a workflow? (It makes decisions at runtime: which tool, whether to continue.)

## 10. "Can I write this from memory?" checklist
- [ ] I can write the full agent in under 60 lines
- [ ] I can explain each block (state, tools, loop, memory)
- [ ] I can add a new tool
- [ ] I can explain loop safety
