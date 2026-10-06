# 17 - Tools

## What is it?

A tool is a function the LLM can request to call. `@tool` builds the tool from a
plain function: the docstring becomes the description, the type hints become the
JSON argument schema.

## Flow

```
Function (add_numbers)
  ↓  @tool
Tool (name + description + args schema)
  ↓  bind_tools
Model decides -> AIMessage with tool_calls
  ↓  (someone executes it)
Result
```

## Code idea

`bind_tools([tool])` attaches the tool schema to the model. The model responds
with `response.tool_calls` instead of executing anything. In an agent, LangChain
executes the calls and feeds results back (project 18).

## Important lines

```python
@tool
def add_numbers(a: int, b: int) -> int:
    """Add two numbers together."""
    return a + b

model_with_tools = model.bind_tools([add_numbers])
response.tool_calls   # what the model wants to call
```

## Interview question

1. How do you create a tool?
2. What becomes the tool's schema?
3. Who executes the tool?

## Interview answer

1. `@tool` on a function with type hints and a docstring.
2. Docstring = description; type hints/args = JSON schema.
3. The model only REQUESTs a call; your code (or the agent) executes it.

## Remember

- Tool != agent. A tool is just a schema + function.
- `tool_calls` appear on the AIMessage.
- Type hints and docstrings are the tool contract - write them well.
