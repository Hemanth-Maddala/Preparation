"""
Project 01 - Basic StateGraph
=============================
The smallest possible LangGraph program.

Graph:  START -> greeting_node -> END

Run:  python main.py
"""

## Q. Why typeddict used from typing ? and why not using Basemodel in pydantic
## A. In LangGraph, TypedDict is generally better and more standard for defining graph state, while Pydantic BaseModel is better suited for runtime validation at node boundaries or handling structured inputs/outputs.
## simply -> typeddict is used for defining the schema of the state (what it should carries between the states) , it is lightweight and fast
## pydantic is also used to define schema of state , but slow compared to typeddict , it do the runtime validation of the paramters 
## we can implement reducerrs using the annotated from typing  -> in both typeddict,pydantic

# 1. State: a TypedDict that describes ALL data that flows through the graph.
#    Every node receives `state` and can return updates to it.
from typing import TypedDict
from langgraph.graph import StateGraph, START, END


class State(TypedDict):
    # The graph will only ever hold these keys.
    name: str
    greeting: str


# 2. Node: a normal Python function.
#    It receives the current `state` (a dict) and returns updates (a dict).
#    Only the keys you return are written into the graph state.
def greeting_node(state: State):
    print(">>> running greeting_node")
    return {"greeting": f"Hello, {state['name']}!"}


# 3. Build the graph.
builder = StateGraph(State)

# 4. Register the node with the graph.
builder.add_node("greeting_node", greeting_node)

# 5. Edges: START -> node -> END.
builder.add_edge(START, "greeting_node")
builder.add_edge("greeting_node", END)

# 6. compile() turns the graph spec into a runnable compiled graph.
app = builder.compile()


# 7. invoke() runs the graph once with the given input state.
if __name__ == "__main__":
    result = app.invoke({"name": "Hemanth"})
    print("\nFinal state:", result)
