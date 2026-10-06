# 20 - Structured agent

## What is it?

A structured agent is an agent that returns a validated Pydantic object instead
of free text. Add `response_format=Schema` to `create_agent`; the result lands in
`result["structured_response"]`.

## Flow

```
Agent loop (tools + model)
  ↓
response_format=Answer
  ↓
Validated Answer object (answer + confidence)
```

## Code idea

Define the `BaseModel` class, pass it to `create_agent(response_format=Answer)`,
then read `result["structured_response"]`. Same idea as `with_structured_output`
but for the whole agent.

## Important lines

```python
class Answer(BaseModel):
    answer: str
    confidence: float

agent = create_agent(model=model, tools=[...], response_format=Answer)
answer = result["structured_response"]
```

## Interview question

1. How do you make an agent return structured output?
2. Where is the result stored?
3. Structured model call vs structured agent?

## Interview answer

1. Pass a Pydantic class as `response_format` to `create_agent`.
2. In `result["structured_response"]`.
3. A model call is one response; an agent can call tools first, then still
   returns structured output.

## Remember

- `response_format` on create_agent = `with_structured_output` for agents.
- The object is validated by Pydantic.
- Combine with tools freely.
