# Project 01 - Basic StateGraph

## 1. What this project teaches
The absolute minimum LangGraph program: State, StateGraph, one node, START, END, compile(), invoke().

## 2. Problem statement
Print "Hello, <name>!" using a LangGraph graph instead of a plain function.

## 3. LangGraph concept being demonstrated
- **State**: a TypedDict describing every piece of data the graph works with.
- **StateGraph**: the container where nodes and edges are registered.
- **Node**: a plain Python function that reads state and returns updates.
- **START**: the special entry point of the graph.
- **END**: the special exit point of the graph.
- **compile()**: builds a runnable graph from the builder.
- **invoke()**: runs the graph once with input state.

## 4. Simple architecture / graph diagram

```
 Input {"name": "Hemanth"}
        |
        v
     START
        |
        v
 greeting_node   (returns {"greeting": "Hello, Hemanth!"})
        |
        v
       END
        |
        v
 Output {"name": "Hemanth", "greeting": "Hello, Hemanth!"}
```

## 5. Step-by-step execution flow
1. `app.invoke({"name": "Hemanth"})` is called with input state.
2. Execution starts at `START`.
3. Edge START -> greeting_node moves control to `greeting_node`.
4. `greeting_node` reads `state["name"]` and returns `{"greeting": ...}`.
5. That update is merged into the state.
6. Edge greeting_node -> END finishes the run.
7. `invoke()` returns the final full state.

## 6. Important code explanation
- `State(TypedDict)`: declares the shape of state. Only these keys can be written.
- `greeting_node(state)`: the node. It returns a dict of key -> value updates.
- `StateGraph(State)`: create a builder for state of this shape.
- `add_node`: give the graph a named node.
- `add_edge(START, "node")` and `add_edge("node", END)`: define the flow.
- `compile()`: REQUIRED before use. Without it there is no runnable graph.
- `invoke(state)`: runs the graph and returns the final state.

## 7. Expected output
```
>>> running greeting_node

Final state: {'name': 'Hemanth', 'greeting': 'Hello, Hemanth!'}
```

## 8. What I should remember for an interview
- A LangGraph app = State + Nodes + Edges + compile().
- A node is just a function: `fn(state) -> state_updates`.
- `invoke()` returns the whole final state, not just the node output.
- START/END are the only special nodes; every graph needs a path START -> ... -> END.

## 9. Possible interviewer questions
- What is a StateGraph?
- What is State?
- What is a node?
- What do START and END mean?
- Why is compile() required?
- What does invoke() do?

## 10. "Can I write this from memory?" checklist
- [ ] I can define a State TypedDict
- [ ] I can write a node function
- [ ] I can create StateGraph(State)
- [ ] I can add_node and add_edge (START and END)
- [ ] I can compile() and invoke()
- [ ] I can draw this graph on paper in 30 seconds

---

## MINIMUM LANGGRAPH CODE I SHOULD REMEMBER FOR AN INTERVIEW

```python
from typing import TypedDict
from langgraph.graph import StateGraph, START, END

class State(TypedDict):
    value: str

def my_node(state: State):
    return {"value": state["value"].upper()}

builder = StateGraph(State)
builder.add_node("my_node", my_node)
builder.add_edge(START, "my_node")
builder.add_edge("my_node", END)
app = builder.compile()

result = app.invoke({"value": "hi"})
print(result)  # {'value': 'HI'}
```

Memorize the order: State -> node function -> StateGraph -> add_node -> add_edge(START..) -> add_edge(..END) -> compile -> invoke.
