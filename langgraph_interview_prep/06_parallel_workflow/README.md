# Project 06 - Parallel Workflow

## 1. What this project teaches
Parallel branches: multiple nodes run in the same superstep and their results are combined afterwards.

## 2. Problem statement
For a destination, gather weather + hotels + activities at the same time, then combine them into one summary.

## 3. LangGraph concept being demonstrated
- Parallel execution (fan-out from START)
- Fan-in (multiple edges into one aggregator)
- How results are combined via State keys
- Sequential vs parallel workflows

## 4. Simple architecture / graph diagram

```
             START
              |
   +----------+----------+
   |          |          |
   v          v          v
 weather   hotels   activities
   |          |          |
   +----------+----------+
              |
              v
         aggregator
              |
              v
             END
```

## 5. Step-by-step execution flow
1. START sends control to all three branches in the same superstep.
2. Each branch writes its own state key (weather, hotels, activities).
3. The aggregator starts only when every incoming edge has finished.
4. Aggregator reads all three keys and writes `summary`.

## 6. Important code explanation
- Fan-out: multiple `add_edge(START, ...)` calls.
- Fan-in: multiple `add_edge(branch, "aggregator")` calls.
- The aggregator's "barrier" is automatic: it runs only after all its predecessor edges complete.
- Each branch updates a DIFFERENT state key, so their updates don't collide.

## 7. Expected output
```
>>> weather (branch 1)
>>> hotels (branch 2)
>>> activities (branch 3)
>>> aggregator (after all branches)

Final summary:
Sunny, 28C in Goa
3 hotels available in Goa
5 activities in Goa
```

## 8. What I should remember for an interview
- **Sequential vs parallel:** sequential runs one node then the next; parallel runs nodes with no dependencies in the same superstep. LangGraph schedules automatically.
- **How are results combined?** Through shared State. Each branch writes its own key; a join node reads all keys.
- Parallel is best for independent sub-tasks (API calls, lookups) that can be done at the same time.
- Same-superstep nodes run on the same snapshot of state; their writes merge afterwards.

## 9. Possible interviewer questions
- How do you run nodes in parallel?
- Why is parallelism useful?
- How do you combine parallel results?
- Can parallel branches share data? (Only via state, after the superstep.)

## 10. "Can I write this from memory?" checklist
- [ ] I can fan out from START to 3 nodes
- [ ] I can fan in to one aggregator
- [ ] I can combine results via state keys
- [ ] I can explain when parallelism helps
