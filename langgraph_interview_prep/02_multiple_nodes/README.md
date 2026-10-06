# Project 02 - Multiple Nodes

## 1. What this project teaches
How to build a chain of multiple nodes, how edges connect them, and how state is passed and updated between nodes.

## 2. Problem statement
Take a raw sentence, clean it, count its words, and produce a formatted output line using three separate nodes.

## 3. LangGraph concept being demonstrated
- Multiple nodes registered on one StateGraph
- Edges that define the chain order
- State passing: every node receives the full state
- State updating: a node only writes back the keys it returns

## 4. Simple architecture / graph diagram

```
 Input {"raw": "  Hello LangGraph World  "}
        |
        v
     START
        |
        v
  preprocess  -> writes "cleaned"
        |
        v
    process    -> writes "count"
        |
        v
  format_output-> writes "output"
        |
        v
       END
```

## 5. Step-by-step execution flow
1. `invoke({"raw": ...})` starts the graph with `raw` only.
2. `preprocess` cleans the text and writes `cleaned`.
3. `process` reads `cleaned`, counts words, writes `count`.
4. `format_output` reads `count`, writes `output`.
5. The final state contains all keys written along the way.

## 6. Important code explanation
- Nodes run in the order defined by edges.
- A node returns only the keys it wants to update. Missing keys stay unchanged.
- `invoke()` returns the accumulated final state, so you can see exactly what each node added.

## 7. Expected output
```
1. preprocess  | raw='  Hello LangGraph World  '
2. process     | cleaned='hello langgraph world'
3. format      | count=3

Final state: {'raw': '  Hello LangGraph World  ', 'cleaned': 'hello langgraph world', 'count': 3, 'output': '3 words'}
```

## 8. What I should remember for an interview
- **"How do you pass information from one node to another?"**
  Answer: nodes communicate ONLY through shared State. Node A returns `{"key": value}`; the framework merges it into state; Node B reads `state["key"]`. No direct function calls between nodes.
- The node function signature is always `fn(state) -> dict of updates`.
- Order of execution = order of edges, not order of definition.

## 9. Possible interviewer questions
- How do you pass data between nodes?
- What happens if a node returns a key that is not in State?
- Can two nodes read each other's output? (Only via shared state.)
- Why not just call Python functions directly?

## 10. "Can I write this from memory?" checklist
- [ ] I can register 2-3 nodes on a graph
- [ ] I can chain them with add_edge
- [ ] I can explain state passing in one sentence
- [ ] I know a node only updates keys it returns
- [ ] I can modify this to a 5-node chain without docs
