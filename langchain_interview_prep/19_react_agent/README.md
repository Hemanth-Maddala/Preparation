# 19 - ReAct agent

## What is it?

ReAct = Reason + Act. The agent thinks, takes an action (tool call), observes
the result, and thinks again until it can answer. This is the loop behind most
LangChain agents.

## Flow

```
Reason -> Act (tool call) -> Observe (result) -> Reason -> ... -> Answer
```

## Code idea

`create_agent` builds this loop for you. Printing all `result["messages"]` shows
the steps: AIMessage with `tool_calls` (the Act), ToolMessage with the result
(the Observe), and finally a plain AIMessage (the Answer).

## Important lines

```python
agent = create_agent(model=model, tools=[multiply], system_prompt="...")
result = agent.invoke({"messages": [...]})
msg.tool_calls   # what the agent decided to call (the Act)
```

## Interview question

1. What does ReAct stand for?
2. Basic agent vs ReAct vs autonomous agent?
3. How many tool calls happen for "3*4, then *2"?

## Interview answer

1. Reasoning and acting in a loop: think, act, observe, repeat.
2. Basic = simple tool loop; ReAct = the explicit think->act->observe pattern;
   autonomous = ReAct at scale (longer loops, more tools, persistence).
3. Two: 3*4 = 12, then 12*2 = 24 - the loop repeats until no tool call remains.

## Remember

- ReAct is the loop, not a special class in modern LangChain.
- The loop ends when the model answers without a tool call.
- The messages list is the memory of every act/observe step.
