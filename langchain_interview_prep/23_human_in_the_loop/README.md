# 23 - Human in the loop

## What is it?

Human in the loop pauses an agent at a chosen point (here: before tools) until a
human approves or rejects. The run is saved by a checkpointer, so it can be
resumed with a decision.

## Flow

```
Agent -> wants to call tool -> PAUSE
                                  ↓ human
Approve (Command(resume=True))  |  Reject
  ↓                             |
tool runs                       stop
  ↓
agent continues
```

## Code idea

`interrupt_before=["tools"]` pauses before tools. `agent.invoke(...)` returns
the paused state; `agent.invoke(Command(resume=True), config)` resumes with
approval. (The `__interrupt__` key with the Interrupt payload only appears when
you call `interrupt()` inside a node yourself.)

## Important lines

```python
agent = create_agent(..., checkpointer=InMemorySaver(), interrupt_before=["tools"])
result = agent.invoke(input, config=config)
result = agent.invoke(Command(resume=True), config=config)
```

## Interview question

1. How do you pause an agent for approval?
2. What is needed to resume?
3. Where can interrupts be placed?

## Interview answer

1. `interrupt_before` (or `interrupt_after`) on create_agent, plus a checkpointer.
2. A checkpointer (to save state) and the same thread_id; resume via Command.
3. Before/after nodes, e.g. before tools, or a custom approval step.

## Remember

- No checkpointer + no thread_id = no resume.
- interrupt_before stops before the node; interrupt() inside a node can attach a payload.
- Command(resume=True) = approve; different values can edit/reject.
