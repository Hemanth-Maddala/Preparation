# Project 08 - ReAct Agent

## 1. What this project teaches
The ReAct pattern (Reason + Act) implemented as a LangGraph loop, with tools and conditional routing.

## 2. Problem statement
Build an agent that answers questions, calling tools (calculator, weather) when it decides they are needed.

## 3. LangGraph concept being demonstrated
- ReAct: Reason -> Act -> Observe -> Repeat
- Tool calls inside an AIMessage
- ToolNode execution
- Conditional routing (tool needed? keep looping : stop)
- Messages state (`add_messages`)
- LLM: real Gemini, key loaded from `.env` (no mock, no hardcoded keys)

## 4. Simple architecture / graph diagram

```
              START
                |
                v
             agent  <-------------------+
                |                        |
    (tool_calls?)                       |
      /        \                        |
     yes        no                      |
     |           |                      |
     v           v                      |
   tools       END                      |
     |                                  |
     +---- observe (ToolMessage) -------+
```

## 5. Step-by-step execution flow (the ReAct cycle)
1. REASON: agent calls the LLM with the conversation so far.
2. The LLM decides: answer directly, OR emit a tool_call.
3. If tool_call -> ACT: `tools` node (ToolNode) runs the tool.
4. OBSERVE: the tool result is appended as a ToolMessage.
5. The edge `tools -> agent` loops back -> REASON again with the new observation.
6. When the LLM finally answers without a tool_call, routing sends control to END.

## 6. Important code explanation
- `llm.invoke(messages)`: calls real Gemini; it returns AIMessage objects.
- An AIMessage with `tool_calls=[{...}]` means "please run this tool".
- `should_continue` inspects the last message: `tool_calls` -> loop, else END.
- `ToolNode(TOOLS)` executes the requested tool and produces the ToolMessage.
- The ReAct loop (agent -> tools -> agent) is visible in real time; how many turns it takes is decided by Gemini at runtime.

## 7. Expected output
(Real Gemini - exact wording varies, the loop shape stays the same.)
```
[llm] Using Gemini

Q: What is the weather in Paris?
   HumanMessage: What is the weather in Paris?
   AIMessage:  (tool call)
   ToolMessage: Sunny, 28C in Paris
   AIMessage: The weather tool says it is Sunny, 28C in Paris.
```

## 8. What I should remember for an interview
- **What is ReAct?** A pattern where the LLM alternates between Reasoning (thinking) and Acting (calling tools), observing the result, then reasoning again.
- **How does LangGraph implement a ReAct loop?** Two nodes (agent and tools) connected in a cycle. The conditional edge on the agent node decides whether to loop (tool) or stop (END).
- **Why use a graph for a ReAct agent?** The loop, branching, and state are explicit; you can pause, resume, add memory, or add human approval at any point.
- **What happens when the LLM doesn't request a tool?** The routing function sends control to END; the last AIMessage is the final answer.
- **ReAct vs autonomous agent:** ReAct is a reasoning pattern. An autonomous agent is a broader system that can pursue a goal; it may USE a ReAct loop inside it. They are not separate technologies.

## 9. Possible interviewer questions
- What is ReAct?
- How does a ReAct agent work?
- How does LangGraph implement a ReAct loop?
- Why use a graph for a ReAct agent?
- What happens when the LLM doesn't request a tool?
- ReAct vs autonomous agent?

## 10. "Can I write this from memory?" checklist
- [ ] I can define tools and a ToolNode
- [ ] I can write the agent node (llm.invoke)
- [ ] I can write should_continue checking tool_calls
- [ ] I can wire the agent->tools->agent cycle
- [ ] I can explain the Reason/Act/Observe cycle
- [ ] I know how to load the Gemini key from .env (load_dotenv + os.getenv)
