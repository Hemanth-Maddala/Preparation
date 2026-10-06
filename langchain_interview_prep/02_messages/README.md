# 02 - Messages

## What is it?

LangChain represents any conversation as a list of message objects, each with a
role. `SystemMessage` sets behaviour, `HumanMessage` is user input, `AIMessage`
is model output. No memory system is needed for a simple multi-turn call.

## Flow

```
SystemMessage + HumanMessage (+ past AIMessages)
  ↓
Chat Model
  ↓
AIMessage
```

## Code idea

Build a `list` of messages, pass the whole list to `model.invoke(messages)`. The
model treats it as one conversation. Feed the `AIMessage` back in to continue.

## Important lines

```python
messages = [SystemMessage(...), HumanMessage(...)]
response = model.invoke(messages)
conversation = messages + [response, HumanMessage(...)]
```

## Interview question

1. What roles of messages exist in LangChain?
2. Why do models take a list of messages instead of one string?
3. How do you continue a conversation without a memory system?

## Interview answer

1. System, Human, AI (and Tool for tool results in agents).
2. Because a model call is the whole context of the conversation, not one prompt.
3. Keep the list of messages, append the new AIMessage and HumanMessage, and pass
   the whole list again.

## Remember

- Messages are objects with a `role` and `content`.
- The order of the list IS the conversation order.
- No memory = you manage the list yourself.
