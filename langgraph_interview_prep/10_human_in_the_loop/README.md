# Project 10 - Human in the Loop

## 1. What this project teaches
How to pause a workflow for human approval, and how to resume it.

## 2. Problem statement
User requests "Transfer ₹10,000". The workflow must NOT execute until a human approves the transaction.

## 3. LangGraph concept being demonstrated
- Interrupts: `interrupt(value)` pauses the graph mid-run
- Resume: `Command(resume=...)` continues from the pause point
- State preservation across the pause (checkpointing)
- Human-in-the-loop (HITL)

## 4. Simple architecture / graph diagram

```
 START
   |
   v
validate
   |
   v
prepare
   |
   v
approval  <-- interrupt() PAUSES here, asks human
   |              |
   |              +--- resume "yes" ---> execute -> END
   +--- resume "no"  -----------------------> END
```

## 5. Step-by-step execution flow
1. `validate` checks the amount.
2. `prepare` builds the transaction.
3. `approval` calls `interrupt({...})` -> the graph PAUSES. The invoke returns with state saved.
4. The app shows the human the question (in production: a UI).
5. Human approves -> `invoke(Command(resume="yes"), config)`.
6. `interrupt()` returns "yes"; the node routes to `execute` (or END if "no").
7. State from before the pause is still there (nothing is lost).

## 6. Important code explanation
- `interrupt(value)`: returns control to the caller and asks for a value. That value is the argument you pass to `Command(resume=...)`.
- `Command(resume="yes")`: resumes the latest checkpoint of the thread with "yes".
- A checkpointer is REQUIRED: pausing means saving state.
- `Command(goto=..., update=...)` lets the node both route and update state after the human decision.

## 7. Expected output
```
>>> validate transaction
>>> prepare transaction

[paused] status: pending approval
[waiting for human decision...]

>>> execute (mock transfer)

[resumed] status: executed
log: ['validated', 'prepared transfer of 10000 to Savings-123', 'executed (mock)']
```

## 8. What I should remember for an interview
- **How do you pause a LangGraph workflow?** Call `interrupt(value)` inside a node. It halts execution and returns control with the value exposed.
- **How do you resume it?** Call `invoke(Command(resume=value), config)` on the same thread. The interrupt returns that value.
- **Why is human-in-the-loop useful for AI agents?** AI makes mistakes; for money, medical, or sensitive actions you want a human gate. Also useful for approval, review, or gathering missing info.
- Interrupt requires a checkpointer (state must persist so it can be restored).
- Each `interrupt` gets an id; `Command(resume={id: value})` targets a specific one.

## 9. Possible interviewer questions
- How do you pause a LangGraph workflow?
- How do you resume it?
- Why is human-in-the-loop useful for AI agents?
- Why is a checkpointer required for interrupts?
- Can you have multiple interrupt points? (Yes, with ids.)

## 10. "Can I write this from memory?" checklist
- [ ] I can use interrupt() to pause
- [ ] I can resume with Command(resume=...)
- [ ] I remember a checkpointer is mandatory
- [ ] I can explain the approve/deny flow
