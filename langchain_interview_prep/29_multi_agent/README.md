# 29 - Multi-agent

## What is it?

A multi-agent system has several agents with different roles. A supervisor
decides which specialist handles a request. Here the supervisor routes to a
research agent and/or a writer agent - each is just a small function that calls
the model with its own system prompt.

## Flow

```
User -> Supervisor
         ├── RESEARCH -> research agent -> writer agent -> answer
         └── WRITE    -> writer agent -> answer
```

## Code idea

Each agent = prompt + model (a tiny chain). The supervisor is another small
chain that returns a decision word, and plain Python `if` routes the work. Real
Gemini calls throughout.

## Important lines

```python
decision = (route_prompt | model).invoke({"question": question}).content
if "RESEARCH" in decision:
    return writer_agent(research_agent(question))
```

## Interview question

1. What is a multi-agent system?
2. What is the role of the supervisor?
3. How do the agents communicate?

## Interview answer

1. Several agents with different roles collaborating on one request.
2. Routing: deciding which specialist (or sequence) handles the task.
3. Through their inputs/outputs - one agent's return value is the next agent's
   prompt (in a graph, through shared state).

## Remember

- Roles = different system prompts.
- The supervisor is just another model call returning a decision.
- Start simple: supervisor + 2 specialists is enough for an interview.
