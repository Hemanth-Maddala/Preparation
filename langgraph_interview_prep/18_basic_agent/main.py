"""
Project 18 - Basic AI Agent
===========================
What makes something an AI AGENT instead of just a workflow?

In a NORMAL LangGraph WORKFLOW the developer hard-codes the path:
    Node A -> Node B -> Node C   (always the same)

In a BASIC AGENT the LLM decides the next action:
    User -> LLM -> (use a tool?) -> tool -> result -> LLM -> final answer

The agent's graph is a tiny LOOP:

              USER
                |
                v
             AGENT
                |
        +-------+--------+
        |                |
  (tool call?)    (normal answer)
        |                |
        v                v
      TOOLS           END
        |          (final answer)
        v
     AGENT  (again, now with the tool result)
        |
        v
     END (final answer)

The tools (calculator / weather / knowledge) are real Python functions.
The LLM only DECIDES which one to call - it never executes Python itself.

LLM: real Gemini via the Google GenAI SDK, key + model from `.env`.
     No mock LLM, no hardcoded keys. See `llm.py`.

Run:
  copy .env.example .env   (put your GEMINI_API_KEY inside)
  python main.py
"""

from typing import Annotated, Literal, TypedDict

from langchain_core.messages import HumanMessage
from langchain_core.tools import tool
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode
from dotenv import load_dotenv

from llm import AgentLLM

load_dotenv()


# ---------- 1. Tools (real Python functions) ----------

@tool
def calculator_tool(expression: str) -> str:
    """Evaluate a safe arithmetic expression like '25 * 16'."""
    return str(eval(expression, {"__builtins__": {}}))


@tool
def weather_tool(city: str) -> str:
    """Return a deterministic weather report for a city."""
    return f"Sunny, 28C in {city}"


@tool
def knowledge_tool(topic: str) -> str:
    """Look up a short fact from a local knowledge dictionary."""
    knowledge = {
        "langgraph": "LangGraph is a library for building stateful LLM agents as graphs.",
        "react": "ReAct = Reason + Act: alternate thinking and tool calls.",
        "agent": "An AI agent is an LLM-powered system that decides actions, uses tools, observes results, and produces an answer.",
    }
    for key, value in knowledge.items():
        if key in topic.lower():
            return value
    return f"No local knowledge found for '{topic}'."


TOOLS = [calculator_tool, weather_tool, knowledge_tool]


# ---------- 2. Real LLM (Gemini via GenAI SDK, key from .env) ----------

llm = AgentLLM(tools=TOOLS)

SYSTEM_PROMPT = (
    "You are a personal assistant. Call a tool ONLY when it provides the exact "
    "data you need: calculator_tool for arithmetic, weather_tool for weather, "
    "knowledge_tool for local facts. Otherwise answer directly from your "
    "knowledge, without using a tool."
)


# ---------- 3. State (message-based - the whole conversation) ----------

class State(TypedDict):
    # add_messages makes the list APPEND instead of overwrite: every
    # HumanMessage, AIMessage and ToolMessage is kept in order.
    messages: Annotated[list, add_messages]


# ---------- 4. Nodes ----------

def agent(state: State):
    """Send the conversation to Gemini. THE MODEL DECIDES whether the reply
    is a normal answer or a tool call. We do not force any action."""
    response = llm.invoke(state["messages"], system=SYSTEM_PROMPT)
    return {"messages": [response]}


def should_use_tool(state: State) -> Literal["tools", "__end__"]:
    """Conditional routing based on the LLM's decision:
       - the last AIMessage contains tool_calls  -> run the tool(s)
       - otherwise                              -> the answer is final"""
    last = state["messages"][-1]
    if getattr(last, "tool_calls", None):
        return "tools"
    return END


# ---------- 5. Build the graph ----------

builder = StateGraph(State)
builder.add_node("agent", agent)
builder.add_node("tools", ToolNode(TOOLS))  # executes the requested tools

builder.add_edge(START, "agent")
builder.add_conditional_edges("agent", should_use_tool, {"tools": "tools", END: END})
builder.add_edge("tools", "agent")  # tool result goes back to the LLM

app = builder.compile()

if __name__ == "__main__":
    questions = [
        "What is 25 * 16?",
        "What is the weather in Hyderabad?",
        "Tell me about LangGraph.",
    ]
    for question in questions:
        print(f"\nQ: {question}")
        result = app.invoke({"messages": [HumanMessage(content=question)]})
        for message in result["messages"]:
            content = message.content or "(tool call)"
            print(f"   {type(message).__name__}: {content}")
        print(f"   FINAL ANSWER: {result['messages'][-1].content}")
