# Project 04 - Conditional Routing

## 1. What this project teaches
Conditional edges, routing functions, branching workflows, and how to implement if/else logic in LangGraph.

## 2. Problem statement
Classify a user request as travel / food / other and route it to the correct handler node.

## 3. LangGraph concept being demonstrated
- Conditional edges via `add_conditional_edges`
- Routing function: a function that returns a string
- Branching: one node can lead to several different nodes

## 4. Simple architecture / graph diagram

```
  request
     |
     v
 classify --> "travel" --> travel_node
     |                          |
     +--> "food"  --> food_node |
     |                          |
     +--> "other" --> other_node
                              |
                              v
                             END
```

## 5. Step-by-step execution flow
1. `classify` sets `state["category"]`.
2. `add_conditional_edges("classify", route_after_classify, {...})` runs.
3. `route_after_classify` reads the category and returns a STRING, e.g. `"travel"`.
4. LangGraph looks up `"travel"` in the path map -> `"travel_node"`.
5. Only `travel_node` runs, then END.

## 6. Important code explanation
- Normal edge: `add_edge("a", "b")` - always goes to b.
- Conditional edge: `add_conditional_edges("a", fn, {value: node})`.
  - `fn(state)` returns one of the keys in the dict.
  - The dict maps the key to the actual node name.
- The routing function is just Python: any if/else or lookup logic is fine.

## 7. Expected output
```
>>> classify
Request: 'Plan a trip to Goa'
Category: travel
Answer: Travel help: best flights to Plan a trip to Goa

>>> classify
Request: 'Find a pizza place'
Category: food
Answer: Food help: here are restaurants for Find a pizza place

>>> classify
Request: 'Tell me a joke'
Category: other
Answer: General help about: Tell me a joke
```

## 8. What I should remember for an interview
- **What are conditional edges?** Edges whose target is decided at runtime by a function.
- **How do they differ from normal edges?** Normal edges have one fixed target; conditional edges choose between several.
- **How does a routing function work?** `fn(state) -> str`, where the str is a key in the path map dict that points to a node name.
- **How do you do if/else in LangGraph?** The routing function IS the if/else logic.
- If the routing function returns a key NOT in the map, LangGraph raises an error.

## 9. Possible interviewer questions
- What are conditional edges?
- Normal vs conditional edge?
- How does a routing function work?
- What happens if the routing function returns an unknown value?
- Can a conditional edge go to END? (Yes: use `END` as a value or as a key.)

## 10. "Can I write this from memory?" checklist
- [ ] I can write `add_conditional_edges("node", route_fn, {..: "node_name"})`
- [ ] I can write a routing function returning a string
- [ ] I can route one of three branches to END
- [ ] I can explain the difference vs normal edges
- [ ] I know the map keys must match the routing function's return values
