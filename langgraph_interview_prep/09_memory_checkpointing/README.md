# Project 09 - Memory / Checkpointing

## 1. What this project teaches
The difference between State and persistence, checkpointing, thread_id, and how to give an agent conversation memory.

## 2. Problem statement
User says "My name is Hemanth." Later asks "What is my name?" The assistant must remember the name across separate invokes.

## 3. LangGraph concept being demonstrated
- State vs persistence
- Checkpointing: saving the full state after every superstep
- `thread_id`: identifies a conversation
- `MemorySaver`: in-memory checkpointer
- Conversation history via `add_messages`

## 4. Simple architecture / graph diagram

```
 invoke (turn 1)  ---> assistant --> END
                          |
                    checkpoint SAVES state + messages
                          |
 invoke (turn 2, same thread_id) --> assistant (sees restored history) --> END
```

## 5. Step-by-step execution flow
1. `invoke({"messages": ["My name is Hemanth."]}, config)` runs `assistant`.
2. The graph saves a checkpoint of the full state after that step.
3. `invoke({...}, config)` again with the SAME thread_id restores the saved state, so `messages` already contains turn 1.
4. The assistant reads the history and answers "What is my name?" correctly.

## 6. Important code explanation
- `builder.compile(checkpointer=MemorySaver())` is what makes state persist. Without it, every invoke starts from a blank state.
- `config = {"configurable": {"thread_id": "..."}}` selects which conversation's checkpoints to use.
- `add_messages` keeps messages append-only; history accumulates.
- **What exactly is being persisted?** The ENTIRE state dict (all keys), not just messages, after every superstep. Next invoke of that thread restores it.
- **Production persistence?** Swap `MemorySaver` for a real store (`SqliteSaver`, Postgres/Redis checkpointer, or LangGraph Platform). The graph code does not change.

## 7. Expected output
(Real Gemini - exact wording varies, the MEMORY behavior is what matters.)
```
--- Turn 1 ---
--- Turn 2 (new invoke, same thread) ---

Turn 2 answer: Nice to meet you, Hemanth! (the model read the persisted history)

Full persisted history for this thread:
  HumanMessage: My name is Hemanth.
  AIMessage: (turn 1 answer)
  HumanMessage: What is my name?
  AIMessage: Nice to meet you, Hemanth! ...
```

## 8. What I should remember for an interview
- **What is checkpointing?** Automatically saving the graph state after each superstep so execution can resume (for memory, human-in-the-loop, fault tolerance).
- **What is thread_id?** A key inside `configurable` that names a conversation/run; state is stored and restored per thread.
- **How is memory implemented in LangGraph?** By checkpointing + a reducer (`add_messages`) that accumulates messages; the LLM reads the full history.
- **Is state automatically persistent?** No. Only if you compile with a checkpointer. The DEFAULT is no persistence.
- **Difference between state and memory?** State = current data dict at a moment. Memory = the ability to carry state across invokes, achieved with checkpointing.

## 9. Possible interviewer questions
- What is checkpointing?
- What is thread_id?
- How is memory implemented in LangGraph?
- Is state automatically persistent?
- Difference between state and memory?
- How would this change for production? (Persistent DB checkpointer)

## 10. "Can I write this from memory?" checklist
- [ ] I know compile(checkpointer=MemorySaver()) enables memory
- [ ] I can use thread_id in config
- [ ] I can explain what gets persisted (the whole state)
- [ ] I can name production checkpointers
- [ ] I can explain state vs memory in one sentence
