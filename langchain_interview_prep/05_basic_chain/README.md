# 05 - Basic chain

## What is it?

A chain connects components so the output of one feeds the next:
prompt -> model -> parser. Built with LCEL (`|`).

## Flow

```
Prompt
  ↓
Model
  ↓
Parser
  ↓
Output
```

## Code idea

Each component is a Runnable. The `|` operator connects them. The input to the
chain is the template variable; the final output is the parsed string.

## Important lines

```python
chain = prompt | model | parser
result = chain.invoke({"text": "..."})
```

## Interview question

1. What is a chain?
2. Why add a StrOutputParser?
3. What is the input and output of a chain?

## Interview answer

1. A pipeline of Runnables where each output becomes the next input.
2. It extracts the plain text from the AIMessage instead of returning the object.
3. Input = what the first component needs (template variables); output = what the
   last component returns (here: a string).

## Remember

- `prompt | model | parser` is the most common chain in LangChain.
- Chains are themselves Runnables: `invoke`, `batch`, `stream` all work.
- Without the parser you get an `AIMessage`, not a `str`.
