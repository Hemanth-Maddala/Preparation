# Project 07 - Tool Calling

## 1. What this project teaches
What a tool is, how tools are defined, how ToolNode executes them, and how tool results get back to the LLM.

## 2. Problem statement
Answer questions that may need outside data (math or weather). When needed, the agent calls a tool and uses its result.

## 3. LangGraph concept being demonstrated
- Tool definition with `@tool`
- Tool invocation via `ToolNode`
- `MessagesState`/`add_messages`: messages are appended, never overwritten
- Tool result returns to the agent as a `ToolMessage`
- Conditional routing: "does it need a tool?"

## 4. Simple architecture / graph diagram

```
 START
   |
   v
 agent
   | \
   |  \  (has tool_call?)
   |   \
   v    v
tools  END
   |
   v
 agent (again, now with tool result)
   |
   v
  END
```

## 5. Step-by-step execution flow
1. User message goes into state as a HumanMessage.
2. `agent` calls the REAL LLM (Gemini, key loaded from `.env`).
3. If the reply contains a tool_call, the routing function sends control to `tools`.
4. `ToolNode` runs the tool and appends a `ToolMessage` (tool result).
5. Edge `tools -> agent` sends the result back; the agent answers using it.

## 6. Important code explanation
- `@tool` turns a plain function into a tool (auto-generated schema + result wrapping).
- `ToolNode(TOOLS)` runs whichever tool the LLM requested.
- `add_messages` reducer makes `messages` append, so history is preserved.
- `getattr(last, "tool_calls", None)` checks whether the last message requests a tool.
- The real LLM shows the "decision": emit a tool_call OR answer directly.

## 7. Expected output
(Real Gemini - exact wording varies, shape stays the same.)
```
[llm] Using Gemini

Q: What is 2+2?
A: 2 + 2 = 4

Q: What is the weather in Paris?
A: The weather tool says: Sunny, 28C in Paris

Q: Hello
A: Hello! How can I help you today?
```

Setup: `copy .env.example .env`, put your `GEMINI_API_KEY` inside, `python main.py`.

## 8. What I should remember for an interview
- **What is tool calling?** The LLM decides it needs external data and emits a structured `tool_call` instead of text; the system executes it and returns the result.
- **Why do agents need tools?** LLMs only know their training data; tools give them calculators, APIs, databases, search.
- **What is ToolNode?** A prebuilt LangGraph node that reads the last AIMessage's `tool_calls` and executes them.
- **How does a tool result get back to the LLM?** As a `ToolMessage` appended to `state["messages"]`, then control returns to the agent node.

## 9. Possible interviewer questions
- What is tool calling?
- Why do agents need tools?
- What is ToolNode?
- How does a tool result get back to the LLM?
- What is add_messages for? (So message history accumulates instead of being overwritten.)

## 10. "Can I write this from memory?" checklist
- [ ] I can define a tool with @tool
- [ ] I can create ToolNode(tools)
- [ ] I can write the should_use_tool routing function
- [ ] I can explain ToolMessage flow
- [ ] I know add_messages appends messages
