"""
Project 11 - Subgraphs
======================
Split a large workflow into smaller, reusable graphs.
A compiled subgraph is used as a NODE in the main graph.

Main graph:
   START -> research_subgraph -> plan_subgraph -> final_response -> END

State flows automatically: the main graph shares state keys with
the subgraphs, so a subgraph can read and write shared fields.

Run:  python main.py
"""

from typing import TypedDict
from langgraph.graph import StateGraph, START, END


# ---------- Shared state between main and sub graphs ----------

class State(TypedDict):
    topic: str
    facts: str
    plan: str
    response: str


# ---------- Research subgraph ----------

def research_node(state: State):
    print("  [research subgraph] gathering facts")
    return {"facts": f"Top 3 facts about {state['topic']}: A, B, C."}


research_builder = StateGraph(State)
research_builder.add_node("research_node", research_node)
research_builder.add_edge(START, "research_node")
research_builder.add_edge("research_node", END)
research_graph = research_builder.compile()  # reusable!


# ---------- Planning subgraph ----------

def plan_node(state: State):
    print("  [plan subgraph] making a plan from facts")
    return {"plan": f"1) Intro  2) Details  3) Summary (based on: {state['facts'][:20]}...)"}


plan_builder = StateGraph(State)
plan_builder.add_node("plan_node", plan_node)
plan_builder.add_edge(START, "plan_node")
plan_builder.add_edge("plan_node", END)
plan_graph = plan_builder.compile()  # reusable!


# ---------- Main graph ----------

def final_response(state: State):
    print("[main] writing final response")
    return {"response": f"Facts: {state['facts']}\nPlan: {state['plan']}"}


main_builder = StateGraph(State)
# Using compiled subgraphs as nodes:
main_builder.add_node("research", research_graph)
main_builder.add_node("planning", plan_graph)
main_builder.add_node("final_response", final_response)

main_builder.add_edge(START, "research")
main_builder.add_edge("research", "planning")
main_builder.add_edge("planning", "final_response")
main_builder.add_edge("final_response", END)

app = main_builder.compile()

if __name__ == "__main__":
    result = app.invoke({"topic": "LangGraph", "facts": "", "plan": "", "response": ""})
    print("\n" + result["response"])




# Second way -> invoking the subgraph in the main graph

# from typing import TypedDict
# from langgraph.graph import StateGraph, START, END

# # ==========================================
# # 1. DEFINE THE SUBGRAPH (Child Graph)
# # ==========================================

# # Subgraph uses its own custom state schema
# class SubgraphState(TypedDict):
#     child_input: str
#     child_output: str

# def process_child_data(state: SubgraphState):
#     # Process data inside the subgraph
#     transformed_text = state["child_input"].upper() + "!"
#     return {"child_output": transformed_text}

# # Compile the subgraph
# subgraph_builder = StateGraph(SubgraphState)
# subgraph_builder.add_node("process_child_data", process_child_data)
# subgraph_builder.add_edge(START, "process_child_data")
# subgraph_builder.add_edge("process_child_data", END)
# compiled_subgraph = subgraph_builder.compile()


# # ==========================================
# # 2. DEFINE THE PARENT GRAPH WITH WRAPPER NODE
# # ==========================================

# # Parent graph uses a completely different state schema
# class ParentState(TypedDict):
#     raw_query: str
#     final_result: str

# # This wrapper node acts as the bridge between different states
# def call_subgraph_node(state: ParentState):
#     # Step A: Map parent state to subgraph input format
#     subgraph_input = {"child_input": state["raw_query"]}
    
#     # Step B: Invoke the compiled subgraph synchronously
#     subgraph_response = compiled_subgraph.invoke(subgraph_input)
    
#     # Step C: Map subgraph output back to parent state format
#     return {"final_result": subgraph_response["child_output"]}

# # Compile the parent graph
# parent_builder = StateGraph(ParentState)
# parent_builder.add_node("subgraph_wrapper", call_subgraph_node)
# parent_builder.add_edge(START, "subgraph_wrapper")
# parent_builder.add_edge("subgraph_wrapper", END)
# compiled_parent = parent_builder.compile()


# # ==========================================
# # 3. EXECUTE THE PARENT GRAPH
# # ==========================================
# if __name__ == "__main__":
#     initial_parent_state = {"raw_query": "hello world"}
#     output = compiled_parent.invoke(initial_parent_state)
#     print(output)
#     # Output: {'raw_query': 'hello world', 'final_result': 'HELLO WORLD!'}
