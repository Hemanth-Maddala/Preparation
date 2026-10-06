# Project 18 - Basic AI Agent

## The conceptual gap this project fills

Projects 01-07 teach LangGraph **workflows**: the developer draws a fixed graph
and the execution path is predetermined (`Node A -> Node B -> Node C`). Projects
08+ jump straight into ReAct, autonomous agents and multi-agent systems. This
project answers the missing question: **what makes a workflow become an AI
agent?**

```
LangGraph Workflow  ->  Basic AI Agent  ->  ReAct Agent  ->  Autonomous Agent  ->  Multi-Agent System
```

A basic agent is the smallest system where **the LLM - not the developer -
decides what to do next**. That single idea is the bridge between a workflow and
everything that follows.

---

## 1. What is an AI agent?

> An AI agent is an LLM-powered system that can **decide what action to take**,
> optionally **use tools**, **observe the results**, and **produce an answer**.

Four moving parts, all present in this project:

1. **Perception** - it reads a message (or state) from the user.
2. **Decision** - the LLM decides the next action ("call a tool" or "answer now").
3. **Action** - a tool executes (a real Python function runs).
4. **Observation + response** - the tool result goes back to the LLM, which
   produces the final answer.

The emphasis is on the word **decide**. A workflow runs a prewritten script. An
agent reads its situation and picks the next step.

## 2. Why is this different from a normal LangGraph workflow?

| | Normal Workflow (projects 01-07) | Basic Agent (this project) |
|---|---|---|
| Who controls the path? | The **developer** | The **LLM** |
| Edges | Hard-coded: `A -> B -> C` always runs | `agent -> tools` **only if the LLM asks** |
| Branching | Pre-planned at design time | Decided at runtime, per message |
| Turns | Fixed sequence | Variable: 1 LLM call, or 2+ (tool round-trip) |

In a workflow the developer writes *"do this, then that, then stop"*. In an
agent the developer writes *"read the conversation, ask the LLM what to do, run
whatever it requests, and stop when it produces an answer"*.

## 3. Architecture diagram

```
              USER
                |
                v
             AGENT  <-------------------------+
                |                              |
        +-------+--------+                     |
        |                |                     |
  (tool call?)     (normal answer)             |
        |                |                     |
        v                v                     |
      TOOLS           END                      |
        |        (final answer)                |
        |                                      |
        +--- result (ToolMessage) -------------+   (agent runs again, now with the tool result)
```

One loop, two nodes: `agent` (Gemini decides) and `tools` (Python executes).

## 4. What the LLM does

The LLM (Gemini) is the **decision-maker**, not the executor. Given the
conversation so far, it produces either:

- a **normal answer** (text), or
- a **tool call** (`tool_calls`) describing *which tool* to run and *with what
  arguments*.

Gemini does NOT run any code. It only emits a structured request like
`call calculator_tool(expression="25 * 16")`. The project's `llm.py` translates
the conversation into Gemini format, calls the API, and translates Gemini's
answer back into a LangGraph `AIMessage` that LangGraph can route on.

## 5. What the tools do

Tools are **plain Python functions** decorated with `@tool`:

- `calculator_tool(expression)` - evaluates a safe arithmetic expression.
- `weather_tool(city)` - returns a deterministic weather report (no external API).
- `knowledge_tool(topic)` - looks up a short fact in a local dictionary.

The tools contain zero "intelligence". They just compute. The intelligence lives
in the LLM deciding *whether* and *which* tool to call.

## 6. How tool calling works

1. The tools are bound to the LLM at startup: `llm = AgentLLM(tools=TOOLS)`.
   `llm.py` turns each `@tool` into a Gemini **function declaration** (name,
   description, parameter schema).
2. When the user asks for math, Gemini sees `calculator_tool` in its tool list
   and emits a `function_call` part.
3. `llm.py` converts that into an `AIMessage` with `tool_calls=[{name, args, id}]`.
4. LangGraph's `ToolNode(TOOLS)` matches the name, calls the real Python
   function, and stores the result in a `ToolMessage`.

**Why doesn't the LLM just run the Python itself?** Because an LLM has no code
execution engine - it generates text. If it "evaluated" `25 * 16` by itself it
could guess wrong. The safe, testable way is: the LLM *decides* which tool to
call, and the *actual Python function* performs the operation. This separation
is what makes tool use auditable and reliable.

## 7. How conditional routing works

```python
def should_use_tool(state: State) -> Literal["tools", "__end__"]:
    last = state["messages"][-1]
    if getattr(last, "tool_calls", None):
        return "tools"
    return END
```

The router reads the **LLM's decision**:

- Last `AIMessage` has `tool_calls` -> run `tools`.
- Last `AIMessage` is plain text -> that text IS the final answer -> `END`.

So the chain is: **LLM decision -> conditional routing -> tool OR final answer**.

## 8. What is stored in state / messages

The state is one field: `messages` (a list of LangGraph message objects).

```python
class State(TypedDict):
    messages: Annotated[list, add_messages]
```

`add_messages` makes the list **append** instead of overwrite. After a full run
the state contains, in order:

| Message type | Meaning | Example |
|---|---|---|
| `HumanMessage` | the user's question | "What is 25 * 16?" |
| `AIMessage` (with `tool_calls`) | the LLM's decision | `call calculator_tool` |
| `ToolMessage` | the tool result | "400" |
| `AIMessage` (plain text) | the final answer | "25 * 16 = 400" |

That history is what the LLM reads on every turn - it is the agent's working
memory within one request.

## 9. Complete execution flow

Example: `"What is 25 * 16?"`

1. `HumanMessage("What is 25 * 16?")` goes into `state["messages"]`.
2. `agent` node sends the messages to Gemini.
3. Gemini decides it needs exact math -> returns a `function_call` to
   `calculator_tool(expression="25 * 16")`.
4. `should_use_tool` sees `tool_calls` -> routes to `tools`.
5. `ToolNode` runs the real Python function -> `"400"` becomes a `ToolMessage`.
6. Edge `tools -> agent`: the agent node runs again, now seeing the tool result.
7. Gemini reads `"400"` and answers `"25 * 16 = 400"` (no tool call).
8. `should_use_tool` sees no `tool_calls` -> `END`.

For `"Tell me about LangGraph."` steps 3-6 never happen: Gemini answers directly
on the first call and the graph ends immediately.

## 10. Example interaction

```
Q: What is 25 * 16?
   HumanMessage: What is 25 * 16?
   AIMessage:  (tool call)
   ToolMessage: 400
   AIMessage: 25 * 16 = 400
   FINAL ANSWER: 25 * 16 = 400

Q: What is the weather in Hyderabad?
   HumanMessage: What is the weather in Hyderabad?
   AIMessage:  (tool call)
   ToolMessage: Sunny, 28C in Hyderabad
   AIMessage: The weather tool says it is Sunny, 28C in Hyderabad.

Q: Tell me about LangGraph.
   HumanMessage: Tell me about LangGraph.
   AIMessage: LangGraph is a library for building stateful LLM agents as graphs.
```

(Real Gemini - exact wording varies; the *shape* - tool round-trip vs direct
answer - is what to observe.)

## 11. How to run

```
pip install -r requirements.txt
copy .env.example .env      # on PowerShell / Command Prompt
# then open .env and put your real key:
#   GEMINI_API_KEY=your_key
#   GEMINI_MODEL=gemini-2.5-flash   (optional)
python main.py
```

The key is read by `llm.py` with `load_dotenv()` + `os.getenv("GEMINI_API_KEY")`.
No credentials are hardcoded.

## 12. Important code sections

- **`llm.py`** - `AgentLLM.invoke(messages, system)` is the only LLM interface.
  It wraps the Google GenAI SDK and translates LangGraph messages <-> Gemini
  contents, converting the model's `function_call` into `AIMessage.tool_calls`.
- **`main.py` - tools**: three `@tool` functions; `TOOLS = [...]`.
- **`main.py` - `llm = AgentLLM(tools=TOOLS)`**: binds the tools so Gemini knows
  what it can call.
- **`main.py` - `agent` node**: sends the conversation to Gemini and returns the
  model's reply (answer OR tool call).
- **`main.py` - `should_use_tool`**: the conditional route on the LLM's decision.
- **`main.py` - `builder.add_edge("tools", "agent")`**: closes the loop so the
  tool result comes back to the LLM for the final answer.

## 13. What I should memorize

- An agent = LLM + (optional tools) + a loop where the **LLM decides**.
- The graph is tiny: `agent` and `tools`, connected in a loop.
- Routing is just "does the last AIMessage contain `tool_calls`?".
- The LLM **decides**, the Python function **executes**, the LLM **answers**.
- `add_messages` keeps the whole conversation as the agent's context.
- A tool-using agent is already an agent. ReAct is one *particular iterative
  pattern* for implementing agent behavior - not a synonym for "agent".

## 14. Interview questions

See the dedicated section below.

---

## INTERVIEW QUESTIONS

1. **What is an AI agent?**
   An LLM-powered system that decides what action to take, can use tools,
   observes the results, and produces an answer. In this project: the agent node
   asks Gemini what to do; Gemini either calls a tool or answers directly.

2. **What makes a system an agent?**
   Autonomy of decision: the system chooses its next action at runtime based on
   its input/state, instead of following a fixed script. Here Gemini chooses
   between "call a tool" and "answer" on every turn.

3. **Is every LangGraph workflow an agent?**
   No. A workflow has a fixed path chosen by the developer (projects 01-07). An
   agent has at least one decision point controlled by an LLM. Most real systems
   are a mix: workflows with LLM decision points inside them.

4. **What is the difference between a workflow and an agent?**
   Control of the next step. Workflow = developer decides, path is fixed.
   Agent = LLM decides, path depends on the conversation. In this project the
   edge `agent -> tools` is only taken when Gemini asks for a tool.

5. **What role does the LLM play in an agent?**
   Decision-maker. It reads the conversation and decides the next action
   (a tool call or a final answer). It does not execute anything itself.

6. **What is tool calling?**
   The LLM returning a structured request (`name` + `args`) describing which
   function to run and with what arguments, instead of (or alongside) text.
   Here Gemini emits `function_call` parts that `llm.py` turns into
   `AIMessage.tool_calls`.

7. **Who executes the tool - LLM or Python?**
   Python. In this project `ToolNode(TOOLS)` finds the requested `@tool` and
   calls the actual function. The LLM only emits the request.

8. **How does the agent decide which tool to use?**
   The tool list is bound to the model (`AgentLLM(tools=TOOLS)`), so Gemini
   knows each tool's name, description and schema. Based on the question it
   picks the matching tool, or none at all.

9. **How does LangGraph route the tool call?**
   `should_use_tool` inspects the last `AIMessage`: if it has `tool_calls`,
   the conditional edge routes to the `tools` node; otherwise it routes to
   `END`.

10. **What happens after the tool returns?**
    The result becomes a `ToolMessage` appended to `messages`, and the edge
    `tools -> agent` sends it back to Gemini, which produces the final answer.

11. **What is the agent loop?**
    The repeated cycle agent -> (maybe tools) -> agent until the LLM produces a
    plain answer. In this project the loop is `agent -> tools -> agent`, and it
    ends when an `AIMessage` has no `tool_calls`.

12. **Is this project a ReAct agent?**
    It has a single tool round-trip, so it looks like one step of ReAct, but it
    is deliberately NOT built as ReAct. It does not force a Reason -> Act ->
    Observe -> Repeat cycle; it simply runs the tool the model requested, once,
    then finishes. That is the minimal "agent" shape.

13. **What is ReAct?**
    A pattern where the LLM alternates Reason -> Act -> Observe -> Reason -> ...
    until it can answer. Each loop turn is driven by the previous observation.
    (That is exactly what project 08 implements.)

14. **Basic Agent vs ReAct Agent?**
    Basic agent: user -> LLM decides (tool OR answer) -> finish. ReAct: user ->
    Reason -> Act -> Observe -> Reason -> Act -> ... -> finish. A basic
    tool-using agent is already an agent; ReAct is an *iterative reasoning/action
    loop* commonly used to implement agent behavior. ReAct is a stronger
    guarantee: it will keep reasoning/acting until it can answer.

15. **ReAct vs autonomous agent?**
    ReAct is a reasoning pattern. An autonomous agent is a broader goal-directed
    system that can plan, act, observe and re-plan until a goal is met, and it
    may use ReAct as its engine. Related, not separate technologies.

16. **Does an agent have to use tools?**
    No. An agent is defined by decision-making. An LLM that decides a sequence
    of steps with no tools is still an agent; tools just let it act on the world.

17. **Does an agent have to use memory?**
    No. Memory (checkpointing, as in project 09) improves an agent but is not
    required. This project keeps the whole conversation in `state["messages"]`
    within one run and needs no cross-run memory.

18. **Does an agent have to be autonomous?**
    "Autonomous" is a spectrum. This basic agent is autonomous for one decision
    (which tool, if any). Fully autonomous agents (project 16) pursue a goal
    across many decisions and can re-plan. Autonomy = how much the LLM decides,
    not a binary flag.

19. **What is the difference between an agent and an LLM call?**
    An LLM call is a single input->output. An agent wraps calls in a loop with
    state, tools, and routing, so the model's output can influence what happens
    next. Here the graph lets Gemini's first answer trigger tool execution and a
    second LLM call.

20. **Why use LangGraph to build the agent?**
    It makes the loop, branching and state explicit and testable: state is data,
    routing is a function, tools are nodes. You can inspect, pause, resume,
    checkpoint, or add human approval - things that are messy with a raw loop.

---

## HOW I WOULD WRITE A BASIC AGENT IN AN INTERVIEW

Minimum conceptual steps:

1. **Define state / messages** - `messages: Annotated[list, add_messages]`.
2. **Create tools** - `@tool` Python functions.
3. **Bind tools to the LLM** - so the model knows it can call them.
4. **Create the agent node** - call the LLM with the conversation.
5. **Create the tool node** - `ToolNode(TOOLS)` executes requested tools.
6. **Add conditional routing** - tool call -> tools, else END.
7. **Connect tool back to agent** - `tools -> agent` closes the loop.
8. **Add END** - the graph terminates when the LLM answers without a tool call.
9. **Compile** - `builder.compile()`.
10. **Invoke** - `app.invoke({"messages": [HumanMessage(content=question)]})`.

Reference skeleton (short enough to memorize):

```python
from typing import Annotated, Literal, TypedDict
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode

@tool
def calculator(expression: str) -> str:
    """Evaluate a safe arithmetic expression like '25 * 16'."""
    return str(eval(expression, {"__builtins__": {}}))

TOOLS = [calculator]

class State(TypedDict):
    messages: Annotated[list, add_messages]

def agent(state: State):
    response = llm.invoke(state["messages"])          # Gemini decides
    return {"messages": [response]}

def route(state: State) -> Literal["tools", "__end__"]:
    last = state["messages"][-1]
    return "tools" if getattr(last, "tool_calls", None) else "__end__"

builder = StateGraph(State)
builder.add_node("agent", agent)
builder.add_node("tools", ToolNode(TOOLS))
builder.add_edge(START, "agent")
builder.add_conditional_edges("agent", route, {"tools": "tools", END: END})
builder.add_edge("tools", "agent")
app = builder.compile()

print(app.invoke({"messages": [HumanMessage(content="What is 25 * 16?")]}))
```

---

## CONCEPTUAL COMPARISON TABLE

Who controls the next step?

| System | Who controls the next step? | Deciding is done... | This project |
|---|---|---|---|
| **Workflow** | The developer | At design time | 01-07 |
| **Basic Agent** | The LLM | At runtime, per message | 18 (this project) |
| **ReAct Agent** | LLM + iterative Reason/Act/Observe loop | At runtime, repeatedly until it can answer | 08 |
| **Autonomous Agent** | LLM/agent pursuing a goal; can plan and re-plan | At runtime, toward a goal | 16 |
| **Multi-Agent System** | Multiple agents coordinate (a supervisor routes work) | At runtime, across specialized agents | 17 |

Read it carefully: these are not five unrelated technologies. It is one idea -
**who decides the next step, and how much** - on an escalating scale:

- A **workflow** has zero LLM decisions (developer chose everything).
- A **basic agent** adds LLM decisions (tool vs answer).
- **ReAct** adds an explicit iterative loop so the LLM reasons/acts repeatedly
  until it can answer.
- An **autonomous agent** adds a goal the agent steers toward, including
  re-planning when things change.
- A **multi-agent system** adds multiple such agents that coordinate through a
  supervisor or handoffs.

Each stage builds on the previous one; they are one continuous progression, not
separate categories.

---

## WHERE THIS FITS IN MY LANGGRAPH LEARNING PATH

- **Projects 01-07** - LangGraph workflows and primitives: state, nodes, edges,
  conditional routing, loops, tools. I learned *how to draw and run graphs*.
- **18_basic_agent** (this project) - what actually makes a workflow an AI
  agent: the LLM starts deciding the next action. This is the bridge.
- **08_react_agent** - iterative reasoning + tool use: Reason -> Act -> Observe
  repeated, the classic pattern for building agent behavior.
- **14_planner_executor** - explicit planning: the agent writes a plan first,
  then executes it step by step.
- **16_autonomous_goal_agent** - goal-directed autonomous behavior: the agent
  keeps deciding, acting and re-planning until a goal is met.
- **17_multi_agent_system** - multiple specialized agents collaborating, with a
  supervisor routing the work.

Together they tell one story: *workflow -> agent decisions -> iterative
reasoning -> goal pursuit -> a team of agents*.
