# Project 14 - Planner + Executor (Plan-and-Execute)

## 1. What this project teaches
The Plan-and-Execute pattern: first plan, then execute the plan step by step.

## 2. Problem statement
User: "Plan a 3-day trip." The system should create a plan (research, activities, schedule), execute each step, and give a final combined answer.

## 3. LangGraph concept being demonstrated
- Planning (LLM produces a list of steps)
- Execution (a loop that runs one step at a time)
- State (plan + index + results)
- Iteration / loop control
- Dynamic task execution

## 4. Simple architecture / graph diagram

```
 START -> planner -> execute_step <--+
                       |             | (more steps)
                       v             |
                 final_response      |
                       |             |
                       v             |
                      END  <---------+
```

## 5. Step-by-step execution flow
1. `planner` asks Gemini to break the task into numbered steps and stores them as `plan` with `index=0`.
2. `execute_step` asks Gemini to DO the current step, appends the result, increments `index`.
3. The routing function checks: `index < len(plan)`? -> loop again : finish.
4. `final_response` joins all step results.

## 6. Important code explanation
- Plan is a LIST in state; `index` tracks progress; `results` is a reducer list.
- Loop = conditional edge back to `execute_step`.
- `MAX_STEPS` caps plan size as a safety guard.
- Both planning AND execution use the real Gemini LLM (key from `.env`) - no mock planner, no mock executor.

## 7. Expected output
(Real Gemini - exact wording varies, the flow shape stays the same.)
```
[llm] Using Gemini
>>> planner
>>> execute step 1: Research the destination
>>> execute step 2: Find activities
>>> execute step 3: Create a schedule
>>> final response

FINAL PLAN RESULT:
Step 1 (Research the destination): <Gemini's research summary>
Step 2 (Find activities): <Gemini's activity list>
Step 3 (Create a schedule): <Gemini's day-by-day schedule>
```

## 8. What I should remember for an interview
- **ReAct vs Plan-and-Execute:** ReAct decides the NEXT action one step at a time after each observation (improvises). Plan-and-Execute creates the full plan FIRST, then executes it (and can re-plan if a step fails). Use Plan-and-Execute when tasks have a clear multi-step structure; use ReAct when each step must react to new information.
- Plan lives in state as data; execution is a loop over that data.
- Executor step output also goes into state so the final node can summarize.

## 9. Possible interviewer questions
- When would you choose Plan-and-Execute instead of ReAct?
- How do you store and iterate over a plan?
- How do you guard the loop? (Plan size cap + index check.)
- Can you re-plan mid-execution? (Yes - a re-planner node on failure.)

## 10. "Can I write this from memory?" checklist
- [ ] I can build a planner that returns a list
- [ ] I can loop over plan steps with an index
- [ ] I can guard the loop against infinite runs
- [ ] I can explain Plan-and-Execute vs ReAct
