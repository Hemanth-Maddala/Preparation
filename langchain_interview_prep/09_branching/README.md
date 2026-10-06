# 09 - Branching

## What is it?

`RunnableBranch` executes one runnable out of several, chosen by a condition
function. It is the if/else of chains.

## Flow

```
            Question
              ↓
RunnableBranch
 ├── condition true  ──> technical prompt -> model
 └── otherwise       ──> general prompt  -> model
```

## Code idea

Pass `(condition_function, runnable)` pairs and end with a fallback runnable.
The condition receives the same dict that will be passed to the branch.

## Important lines

```python
branch = RunnableBranch(
    (is_technical, technical | model),
    general | model,
)
answer = branch.invoke({"question": "..."})
```

## Interview question

1. What is RunnableBranch?
2. What does the condition function receive?
3. How do you add more than two branches?

## Interview answer

1. Conditional runnable execution: pick one path based on a function.
2. The input dict that the chosen runnable will also receive.
3. Add more `(condition, runnable)` pairs before the fallback.

## Remember

- The last argument is the fallback (no condition).
- Conditions run top to bottom; the first true one wins.
- Each branch is itself a full Runnable (often a chain).
