# Project 05 - Loop / Iterative Workflow

## 1. What this project teaches
How LangGraph supports cycles (loops) and how to terminate them safely.

## 2. Problem statement
Generate an answer, evaluate whether it is good enough, and if not, improve it and try again. Stop after a maximum number of iterations.

## 3. LangGraph concept being demonstrated
- Cyclic graphs (an edge that points back to an earlier node)
- Conditional routing as the loop condition
- Loop termination
- Maximum iteration count to avoid infinite loops

## 4. Simple architecture / graph diagram

```
 START
   |
   v
generate_answer
   |
   v
evaluate_answer -------- "improve" -----> improve_answer
   |                                          |
   "good"                                     |
   |                                          |
   v                                          |
  END <---------------------------------------+
```

## 5. Step-by-step execution flow
1. `generate_answer` writes an initial answer.
2. `evaluate_answer` decides: if iteration limit reached -> END ("good"); else "improve".
3. `improve_answer` improves the answer and increments `iteration`.
4. The edge `improve_answer -> generate_answer` loops back.
5. Loop repeats until the condition routes to END.

## 6. Important code explanation
- A loop is just a conditional edge whose target is an earlier node.
- The loop condition lives in the routing function.
- The counter (`iteration`) in state is what guarantees termination.
- The path map uses `END` as a valid target: `{"improve": "improve_answer", "good": END}`.

## 7. Expected output
```
>>> generate (iteration 0)
>>> evaluate: is it good enough?
>>> improve (iteration 0)
>>> generate (iteration 1)
>>> evaluate: is it good enough?
>>> improve (iteration 1)
>>> generate (iteration 2)
>>> evaluate: is it good enough?

Final answer: GoodGoodGood answer about LangGraph. (improved) (improved)
Iterations used: 2
```

## 8. What I should remember for an interview
- **"How would you implement iterative refinement in LangGraph?"**
  Answer: a generate node, an evaluate node, and a conditional edge from evaluate back to generate; the routing function decides loop vs END. Keep a step counter in state and stop when it reaches a max.
- Two guards against infinite loops: a state-based counter/limit and a routing condition that can reach END.
- Reflection (an LLM critiques its own output) is the same shape as this loop, but the evaluator is an LLM.

## 9. Possible interviewer questions
- Can graphs have loops? (Yes - cycles are allowed; the run must end at END.)
- How do you avoid infinite loops?
- How is a loop different from recursion? (Iteration via graph edges, state holds progress.)
- Where would you put the stop condition? (In the routing function.)

## 10. "Can I write this from memory?" checklist
- [ ] I can create a cycle with a conditional edge pointing back
- [ ] I can terminate the loop via routing to END
- [ ] I can add a max-iteration counter
- [ ] I can explain the two loop-exit guards
