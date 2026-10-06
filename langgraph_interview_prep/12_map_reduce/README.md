# Project 12 - Map Reduce / Send

## 1. What this project teaches
Dynamic parallel execution: fan out one task per item in a list, then combine the results.

## 2. Problem statement
Given ["Delhi", "Goa", "Mumbai"], process each city independently (in parallel) and then combine all results into one summary.

## 3. LangGraph concept being demonstrated
- `Send`: tells LangGraph to run a node with specific input
- Dynamic fan-out (number of branches depends on data, not the code)
- Parallel processing of a list
- Aggregation (reduce step)

## 4. Simple architecture / graph diagram

```
            START
              |
              |  map_cities -> [Send x3]
        +-----+------+
        v     v      v
  process_city x 3   (in parallel)
        +-----+------+
              |
              v
        aggregate -> END
```

## 5. Step-by-step execution flow
1. `map_cities` returns `[Send("process_city", {...}), ...]` - one per city.
2. LangGraph launches all of them in parallel in one superstep.
3. Each `process_city` appends one result (the reducer `a+b` accumulates).
4. `aggregate` runs after all maps finish and joins the results.

## 6. Important code explanation
- `Send("node", {"key": value})`: the value is what the node receives as its state.
- `add_conditional_edges(START, map_cities, ["process_city"])`: the conditional function returns Send objects instead of a single string.
- `results: Annotated[list, lambda a, b: a + b]`: a reducer that APPENDS instead of overwriting, so parallel writes don't clobber each other.
- **Normal parallel branches vs map-reduce:** normal branches are FIXED (you write 3 add_edge calls). Map-reduce is DYNAMIC - the number of branches comes from the data at runtime.

## 7. Expected output
```
  processing Delhi
  processing Goa
  processing Mumbai
aggregating all results

Summary: Delhi: 2 days recommended | Goa: 2 days recommended | Mumbai: 2 days recommended
Results: ['Delhi: 2 days recommended', 'Goa: 2 days recommended', 'Mumbai: 2 days recommended']
```

## 8. What I should remember for an interview
- **What is Send?** A command to run a node once, with given input, in parallel. Return a list of Sends from a node to fan out.
- **When would you use Send?** When the number of parallel tasks is only known at runtime (a list of docs to summarize, cities, files, users...).
- **How do you process a dynamic list of tasks?** A fan-out node returns `[Send(node, payload) for item in items]`; a reducer aggregates the results.
- Normal parallel = fixed number of branches in the code; map-reduce = data decides the number of branches.

## 9. Possible interviewer questions
- What is Send?
- When would you use Send?
- How would you process a dynamic list of tasks?
- What is a reducer and why do you need it for fan-in?
- Difference between normal parallel and map-reduce?

## 10. "Can I write this from memory?" checklist
- [ ] I can return a list of Send objects from a node
- [ ] I can wire the map node with a reducer key
- [ ] I can aggregate results
- [ ] I can explain dynamic vs fixed fan-out
