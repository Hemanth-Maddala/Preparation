# Project 03 - Sequential Workflow

## 1. What this project teaches
A realistic multi-step workflow: sequential execution, state updates, and passing information between nodes.

## 2. Problem statement
User says "Plan a trip to Paris for 3 days". The system should extract the destination, find activities, build an itinerary, and write a final response.

## 3. LangGraph concept being demonstrated
- Sequential execution (linear chain of nodes)
- State updates (each node adds one field)
- Passing information between nodes via shared State
- Why a graph is better than one giant function

## 4. Simple architecture / graph diagram

```
 request
    |
    v
extract_destination --> destination
    |
    v
generate_activities --> activities
    |
    v
generate_itinerary --> itinerary
    |
    v
final_response --> response
    |
    v
    END
```

## 5. Step-by-step execution flow
1. `extract_destination` scans the text and finds "paris".
2. `generate_activities` looks up activities for "paris".
3. `generate_itinerary` builds "Day 1 in Paris: ...".
4. `final_response` wraps it in a friendly message.

## 6. Important code explanation
- Each node reads only the fields it needs and writes only what it creates.
- Mock ACTIVITIES dict replaces an LLM so the project runs offline.
- This is exactly how you would design a real pipeline: one node per concern.

## 7. Expected output
```
1. extracting destination
2. generating activities
3. generating itinerary
4. writing final response

Here is your plan:
Day 1 in Paris: Louvre, Eiffel Tower, Seine cruise.
```

## 8. What I should remember for an interview
- **"Why would you use LangGraph for a workflow like this?"**
  Answer: (1) each step is isolated and testable, (2) you can inspect or log state at every point, (3) you can pause, branch, retry or parallelize steps later without rewriting everything, (4) state is explicit and typed instead of hidden inside one function.
- A workflow graph is just a DAG (directed acyclic graph): data flows down edges.

## 9. Possible interviewer questions
- Why a graph instead of a single function?
- How do nodes share data?
- How would you add a validation step in the middle?
- What if extract_destination returns "unknown"?

## 10. "Can I write this from memory?" checklist
- [ ] I can create a 4-node linear pipeline
- [ ] I can explain why LangGraph helps here
- [ ] I can add a new node in the middle of the chain
- [ ] I can draw this graph on paper
