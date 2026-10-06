# 07 - LCEL

## What is it?

LCEL (LangChain Expression Language) is the way to compose Runnables with the
`|` pipe operator. The output of one component is automatically passed as input
to the next. `prompt | model | parser` is the canonical chain.

## Flow

```
prompt (messages)
  ↓ |
model (AIMessage)
  ↓ |
parser (str)
  ↓
result
```

## Code idea

`chain = prompt | model | parser`. `chain.invoke({"topic": "LCEL"})` starts at
the prompt, fills the variable, sends messages to the model, and parses the
answer into a string. The chain is itself a Runnable, so it supports `invoke`,
`batch`, `stream`.

## Important lines

```python
chain = prompt | model | parser
result = chain.invoke({"topic": "LCEL"})
```

## Interview question

1. What is LCEL?
2. How does the `|` operator work?
3. What can you do with a chain besides invoke?

## Interview answer

1. LangChain's composition syntax for building pipelines from Runnables.
2. It connects two Runnables: the output of the left one becomes the input of the
   right one.
3. batch, stream, plus parallel and conditional composition (projects 08/09).

## Remember

- LCEL = `|` composition; the result is still a Runnable.
- Understand which data type flows between every pair of components.
- It is the concept interviewers ask about most.
