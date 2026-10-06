# 06 - Runnable

## What is it?

A Runnable is the common interface of every callable component in LangChain
(models, prompts, parsers, chains, agents, tools). They all support `invoke`,
`batch`, and `stream`.

## Flow

```
Runnable
 ├── invoke(input)   -> one output
 ├── batch(inputs)   -> many outputs
 └── stream(input)   -> chunks of output
```

## Code idea

`RunnableLambda(fn)` turns any plain function into a Runnable so you can call it
with the same interface as a model. The three methods behave identically on
models and chains.

## Important lines

```python
runnable = RunnableLambda(double)
runnable.invoke(4)        # 8
runnable.batch([1, 2, 3]) # [2, 4, 6]
list(runnable.stream(4))  # [8]
```

## Interview question

1. What is a Runnable?
2. Difference between invoke, batch, stream?
3. Why do all components share this interface?

## Interview answer

1. The unit of computation in LangChain; anything you can run.
2. invoke = one in, one out; batch = many in, many out; stream = output in chunks.
3. So components compose with `|` and can be swapped without changing the caller.

## Remember

- `invoke` / `batch` / `stream` (and async versions with an `a` prefix).
- Models, prompts, chains, agents are all Runnables.
- `|` only works between Runnables.
