# 21 - Memory

## What is it?

Memory lets an agent remember earlier turns. The current, simple approach: a
**checkpointer** saves the full state after every run, and a **thread_id**
identifies one conversation. Reusing the thread_id continues that conversation.

## Flow

```
Turn 1 (thread_id = "c1")  -> checkpointer saves state
Turn 2 (thread_id = "c1")  -> agent loads state, remembers turn 1
Turn 3 (thread_id = "c2")  -> new conversation, no memory of c1
```

## Code idea

Pass `checkpointer=InMemorySaver()` to `create_agent` and always send a `config`
with `thread_id`. The full conversation history becomes the agent's context.

## Important lines

```python
agent = create_agent(..., checkpointer=InMemorySaver())
config = {"configurable": {"thread_id": "conversation-1"}}
agent.invoke({"messages": [...]}, config=config)
```

## Interview question

1. How does the current LangChain agent remember a conversation?
2. What is a thread?
3. State vs memory?

## Interview answer

1. A checkpointer persists state; the same thread_id resumes that conversation.
2. One conversation identity; history is stored per thread.
3. State is all data flowing through the graph; memory is the part of state that
   persists across runs (usually messages).

## Remember

- No checkpointer = no memory across runs.
- thread_id decides which conversation history is used.
- Long-term memory (across threads) needs a store - a bigger system; know the
  concept but don't build it in an interview.
