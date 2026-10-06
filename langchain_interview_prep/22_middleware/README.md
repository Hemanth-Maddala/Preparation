# 22 - Middleware

## What is it?

Middleware is code that wraps the agent's steps - before the model, after the
model, around tool calls. Use it for logging, retries, guardrails, or modifying
what reaches the model.

## Flow

```
Agent
 ↓
Middleware (before_model hook)
 ↓
Model call
 ↓
Middleware (after_model hook)
 ↓
Tool calls (wrap_tool_call can wrap these too)
```

## Code idea

Subclass `AgentMiddleware` and override `before_model` / `after_model` hooks.
Pass instances to `create_agent(middleware=[...])`. Hooks receive the current
state and runtime; returning a dict updates the state.

## Important lines

```python
class LoggingMiddleware(AgentMiddleware):
    def before_model(self, state, runtime):
        print(state["messages"][-1].content)
        return None

agent = create_agent(..., middleware=[LoggingMiddleware()])
```

## Interview question

1. What is middleware in an agent?
2. What hooks exist?
3. Give two real uses.

## Interview answer

1. Reusable code that runs around model/tool calls to observe or change them.
2. before_model, after_model, wrap_model_call, wrap_tool_call (and async versions).
3. Logging, retries on failures, PII redaction, cost limits, human approval.

## Remember

- Hooks return state updates (dict) or None.
- Keep it small in an interview: one logging middleware is enough to prove it.
- Built-in middleware exists (PIIMiddleware, retries) - name them.
