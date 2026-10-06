# 30 - LangChain + LangGraph

## What is it?

LangChain provides components (model, prompt, tools); LangGraph provides the
orchestration (state, nodes, routing). Put LangChain components inside a
`StateGraph` and you get full control of the loop. `create_agent` builds exactly
this kind of graph for you automatically.

## Flow

```
START
 ↓
model node (LangChain model)
 ↓ route
 ┌────────────── tools node (LangChain tool)
 └──> no tool_calls -> END
```

## Code idea

Define `State` (a dict with messages), a `call_model` node that invokes the
LangChain model, a `ToolNode`, and a `should_continue` router that goes to tools
when the last message has `tool_calls`, else END. Compile and invoke.

## Important lines

```python
graph.add_node("model", call_model)
graph.add_node("tools", ToolNode([add_numbers]))
graph.add_conditional_edges("model", should_continue)
app = graph.compile()
```

## Interview question

1. Why use LangChain AND LangGraph together?
2. What is the state?
3. How does this relate to create_agent?

## Interview answer

1. LangChain = ready components; LangGraph = custom control flow, loops,
   checkpoints, and human-in-the-loop.
2. The dict of data (here: messages) passed between nodes; nodes return updates.
3. create_agent builds a graph like this under the hood (model + tools + router).

## Remember

- State is the contract of the graph: define it, nodes update it.
- add_messages appends; plain fields overwrite.
- Nodes return partial state updates (dicts), not the whole state.
