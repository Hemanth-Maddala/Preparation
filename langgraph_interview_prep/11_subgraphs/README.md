# Project 11 - Subgraphs

## 1. What this project teaches
How large workflows are split into smaller graphs, and how a compiled subgraph becomes a node in the parent graph.

## 2. Problem statement
Build a workflow that researches a topic, plans an outline, and writes a final response - with research and planning as separate reusable graphs.

## 3. LangGraph concept being demonstrated
- What a subgraph is (a graph used inside another graph)
- Why use subgraphs (reuse, testing, separation of concerns)
- Node vs subgraph (a subgraph behaves like one node from the outside)
- State passing between graphs (shared keys)

## 4. Simple architecture / graph diagram

```
            MAIN GRAPH
   START -> research_subgraph -> plan_subgraph -> final_response -> END
              |                       |
              |__ State.topic         |__ State.facts
                  -> State.facts          -> State.plan
```

## 5. Step-by-step execution flow
1. Main graph starts and runs the `research` node - which is actually `research_graph` compiled.
2. The research subgraph reads `topic`, runs `research_node`, writes `facts`.
3. Control returns to the main graph, which calls the `planning` node (= `plan_graph`).
4. The plan subgraph reads `facts`, writes `plan`.
5. `final_response` combines both fields.

## 6. Important code explanation
- `main_builder.add_node("research", research_graph)`: you add a compiled graph as a node. LangGraph treats it like any other node.
- Subgraph must be `compile()`d before use.
- State sharing: the subgraph's State must include the keys it reads/writes; the main graph's state has the same keys, so data flows in and out automatically.
- A subgraph can also have its OWN extra state keys that never touch the parent.

## 7. Expected output
```
  [research subgraph] gathering facts
  [plan subgraph] making a plan from facts
[main] writing final response

Facts: Top 3 facts about LangGraph: A, B, C.
Plan: 1) Intro  2) Details  3) Summary (based on: Top 3 facts about ...)
```

## 8. What I should remember for an interview
- **What is a subgraph?** A separate compiled StateGraph used as a node inside another graph.
- **Why use subgraphs?** Reusability, unit-testing, readability, and you can use a subgraph in many parent graphs.
- **Node vs subgraph:** from the parent's perspective a subgraph is just a node; but internally it has its own nodes, edges, state, checkpointer.
- State passes via shared keys between parent and child.
- Subgraphs are great for agent teams / multi-agent designs.

## 9. Possible interviewer questions
- What is a subgraph?
- Why use subgraphs?
- Node vs subgraph?
- How does state pass between graphs?
- Can a subgraph have its own checkpointer? (Yes.)

## 10. "Can I write this from memory?" checklist
- [ ] I can build a standalone compiled graph
- [ ] I can add it as a node to a parent graph
- [ ] I can explain shared state between graphs
- [ ] I can give a reason to use subgraphs
