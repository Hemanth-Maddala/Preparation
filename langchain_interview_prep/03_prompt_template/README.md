# 03 - Prompt template

## What is it?

`ChatPromptTemplate` is a reusable prompt with `{variables}`. You define the
template once and fill it with different values every call. No string
concatenation.

## Flow

```
Template ("What is {topic}?")
  ↓  invoke({"topic": "RAG"})
Messages (HumanMessage)
  ↓
Model
  ↓
Answer
```

## Code idea

`ChatPromptTemplate.from_messages([...])` builds a template. `prompt.invoke(dict)`
fills the variables and returns messages. `prompt | model` is LCEL: the prompt's
output (messages) is fed straight into the model.

## Important lines

```python
prompt = ChatPromptTemplate.from_messages([("human", "What is {topic}?")])
messages = prompt.invoke({"topic": "RAG"})
chain = prompt | model
answer = chain.invoke({"topic": "RAG"})
```

## Interview question

1. What is a prompt template for?
2. What input does `prompt.invoke()` take?
3. What does `prompt | model` mean?

## Interview answer

1. Reusing prompts with different variables, instead of building strings manually.
2. A dict with one key per `{variable}` in the template.
3. LCEL pipe: the messages produced by the prompt are passed as input to the model.

## Remember

- Variables are written as `{name}` and filled with a dict.
- `("system", ...)` and `("human", ...)` are shorthand for message constructors.
- `prompt | model` is the basis of every chain.
