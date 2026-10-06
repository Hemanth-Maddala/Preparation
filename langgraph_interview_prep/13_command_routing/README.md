# Project 13 - Command / Dynamic Control Flow

## 1. What this project teaches
`Command`: the current LangGraph API for a node to update state AND choose the next node dynamically.

## 2. Problem statement
Analyze a request (book / cancel / info) and route it to the correct handler - where the node itself makes the routing decision.

## 3. LangGraph concept being demonstrated
- `Command` returned from a node
- Dynamic routing/control flow
- `Command(goto=..., update=...)` - route + update in one step
- When to use Command vs conditional edges

## 4. Simple architecture / graph diagram

```
 START -> analyze ---> (via Command.goto) ---> book_node \
                                                 cancel_node -> execute -> END
                                                 info_node  /
```

## 5. Step-by-step execution flow
1. `analyze` reads the request.
2. It returns `Command(goto="book_node", update={"action": "book"})` (or cancel/info).
3. LangGraph applies the update and runs the target node.
4. The handler writes `result`; `execute` appends "Executed: ...".

## 6. Important code explanation
- `Command(goto=X, update=Y)` combines control flow and state update in one return.
- Return type hint `Command[Literal["book_node", "cancel_node", "info_node"]]` declares which nodes this node can route to (needed for graph visualization/validation).
- `goto` can be a node name, a list, or a `Send`.
- `Command.PARENT` targets the parent graph from inside a subgraph.

## 7. Expected output
```
Request: 'book a flight'
Action: book
Result: Executed: Booking confirmed.

Request: 'cancel my booking'
Action: cancel
Result: Executed: Booking cancelled.

Request: 'show flight info'
Action: info
Result: Executed: Here is the flight information.
```

## 8. What I should remember for an interview
- **What is Command?** A return value a node can use to update state AND navigate (`goto`), resume after an interrupt (`resume`), or send to a parent graph (`graph`).
- **When to use Command instead of conditional edges?** When you need to BOTH update state and route. If you only route, conditional edges are enough. Command also shines for handoffs in multi-agent graphs.
- **What does Command let a node control?** Which node runs next, what state updates are applied, and (with `resume`) how an interrupt is continued.
- Older "return messages + manually route" patterns are replaced by Command in current LangGraph.

## 9. Possible interviewer questions
- What is Command?
- Command vs conditional edges?
- What can a node control with Command?
- What is Command.PARENT used for?
- Does Command work with Send? (Yes: goto can hold Send objects.)

## 10. "Can I write this from memory?" checklist
- [ ] I can return Command(goto=..., update=...) from a node
- [ ] I can annotate the return type with Literal
- [ ] I can explain when to prefer Command over conditional edges
- [ ] I know Command.PARENT and Command(resume=...)
