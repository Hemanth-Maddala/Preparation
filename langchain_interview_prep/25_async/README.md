# 25 - Async

## What is it?

Async versions of every Runnable method: `ainvoke`, `abatch`, `astream`. They
don't block while a slow API call runs, so you can start several calls at once.

## Flow

```
Sync:   invoke(input)   -> block until done
Async:  await ainvoke(input) -> other tasks can run meanwhile
```

## Code idea

`await chain.ainvoke(...)` inside an `async def main()` started by
`asyncio.run(main())`. `asyncio.gather(...)` launches several calls together, so
the total time is the slowest call, not their sum.

## Important lines

```python
one = await chain.ainvoke({"word": "hello"})
results = await asyncio.gather(chain.ainvoke(...), chain.ainvoke(...))
asyncio.run(main())
```

## Interview question

1. How do you call a chain asynchronously?
2. What is asyncio.gather for?
3. When does async actually help?

## Interview answer

1. `await chain.ainvoke(...)` inside an async function, started with
   `asyncio.run()`.
2. Running many awaitable tasks concurrently and collecting all results.
3. When you make many independent LLM calls (multi-turn, parallel branches,
   web services) - I/O time dominates.

## Remember

- Every Runnable has an `a`-prefixed async twin.
- `asyncio.gather` is the one-liner for parallel async calls.
- Don't use async for CPU-bound work.
