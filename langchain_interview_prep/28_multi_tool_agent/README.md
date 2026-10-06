# 28 - Multi-tool agent

## What is it?

An agent with several tools. The LLM reads the question and the tool schemas and
decides which tool (if any) to call. Tool selection is just another decision the
model makes.

## Flow

```
Question "What is 6 * 7?"
  ↓
Agent reads tool schemas
  ↓ chooses
calculator(...)  /  get_weather(...)  /  today()
  ↓ result
Agent answers
```

## Code idea

Define tools with `@tool`, pass all of them to `create_agent`. Each tool needs a
clear name + docstring so the model can tell them apart.

## Important lines

```python
@tool
def calculator(expression: str) -> str: ...

agent = create_agent(model=model, tools=[calculator, get_weather, today], ...)
```

## Interview question

1. How does the agent know which tool to call?
2. What makes tool descriptions matter?
3. What if no tool fits?

## Interview answer

1. It compares the question to each tool's name, description, and arguments.
2. Vague descriptions cause wrong tool choices - be specific.
3. It answers from its own knowledge, or says it cannot answer.

## Remember

- Tool names + descriptions ARE the model's "docs".
- The model can also use several tools in one conversation.
- More tools = harder selection; keep descriptions sharp.
