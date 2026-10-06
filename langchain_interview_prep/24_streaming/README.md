# 24 - Streaming

## What is it?

Streaming delivers output in chunks as the model produces them, instead of
waiting for the whole answer. `invoke()` returns everything at once; `stream()`
yields pieces.

## Flow

```
invoke:  wait ................. [whole answer]
stream:  [token] [token] [token] [token]  (arrives over time)
```

## Code idea

`model.stream(text)` yields `AIMessageChunk`s; print `.content` with
`flush=True`. `agent.stream(input)` yields the agent state after every step,
so you can see the tool call and the final answer as they happen.

## Important lines

```python
for chunk in model.stream("text"):
    print(chunk.content, end="", flush=True)

for step in agent.stream({"messages": [...]}):
    print(step)
```

## Interview question

1. invoke vs stream?
2. Why stream at all?
3. What does agent.stream() yield?

## Interview answer

1. invoke returns one complete result; stream yields chunks over time.
2. Better user experience (first tokens arrive fast) and real-time updates.
3. The state after each agent step (tool calls, intermediate and final messages).

## Remember

- stream() returns a generator; iterate over it.
- flush=True makes printed chunks appear immediately.
- Async version: astream().
