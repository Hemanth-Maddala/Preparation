# 08 - Parallel

## What is it?

`RunnableParallel` fans one input out to several independent branches and runs
them at the same time. The results come back in a dict, one key per branch.

## Flow

```
          Question
          ↓
RunnableParallel
 ├── summary branch ──> summary
 └── keywords branch ─> keywords
          ↓
    combined dict
```

## Code idea

Give each branch a name in the constructor: `RunnableParallel(summary=...,
keywords=...)`. Invoke once with the shared input; read `result["summary"]` and
`result["keywords"]`.

## Important lines

```python
parallel = RunnableParallel(
    summary=summary_prompt | model,
    keywords=keywords_prompt | model,
)
result = parallel.invoke({"topic": "LangChain"})
```

## Interview question

1. What is RunnableParallel for?
2. What does invoke() return?
3. When is it better than doing the calls sequentially?

## Interview answer

1. Running independent tasks concurrently on the same input.
2. A dict keyed by the branch names.
3. When branches don't depend on each other: total time = the slowest branch.

## Remember

- Each key of `RunnableParallel` is a branch.
- The output is a dict, ready to feed into the next component.
- It works with async too (`ainvoke`).
