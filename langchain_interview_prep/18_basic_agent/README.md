# 18 - Basic agent

## What is it?

An agent is an LLM loop: the model reads the conversation, decides whether to
answer directly or call a tool, sees the tool result, and repeats until it is
done. `create_agent` is the current high-level API; it builds a LangGraph loop
for you.

## Flow

```
User
 ↓
Agent (LLM decides)
 ├── answer directly ──────────────> answer
 └── call tool -> tool result -> agent decides again
```

## Code idea

Define tools with `@tool`, pass them plus a system prompt to `create_agent`, then
`agent.invoke({"messages": [...]})`. The final answer is the last message.

## Important lines

```python
agent = create_agent(model=model, tools=[...], system_prompt="...")
result = agent.invoke({"messages": [{"role": "user", "content": "..."}]})
answer = result["messages"][-1].content
```

## Interview question

1. LLM call vs chain vs agent?
2. What does create_agent do?
3. How is the result read?

## Interview answer

1. Model call = one LLM answer; chain = fixed pipeline; agent = loop where the
   LLM decides the steps and calls tools.
2. It assembles model + tools + prompt into a LangGraph loop (reason, call,
   observe, repeat).
3. `result["messages"][-1]` holds the final AIMessage.

## Remember

- The agent EXECUTES tool calls and feeds results back (unlike bind_tools alone).
- LangGraph is underneath create_agent; you don't build the graph manually here.
- System prompt tells the agent WHEN to use tools.
