"""30 - LangChain + LangGraph together.

LangChain = the components: model, prompt, tools, parsers.
LangGraph = the orchestration: State, Nodes, Routing, loops.

Here a LangChain model and tool run inside a LangGraph StateGraph with
a conditional loop - exactly the pattern create_agent builds for you.
"""

import os
from typing import Annotated, TypedDict

from dotenv import load_dotenv
from langchain_core.messages import AnyMessage
from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import END, START, StateGraph
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise SystemExit("Set GEMINI_API_KEY in a .env file (copy .env.example to .env)")

model = ChatGoogleGenerativeAI(
    model=os.getenv("GEMINI_MODEL", "gemini-3.5-flash"),
    api_key=api_key,
)


@tool
def add_numbers(a: int, b: int) -> int:
    """Add two numbers together."""
    return a + b


# 1. LangGraph: STATE = the data that flows between nodes.
#    add_messages appends new messages to the list.
class State(TypedDict):
    messages: Annotated[list[AnyMessage], add_messages]


# 2. LangGraph: NODES = the work. Here they use LangChain components.
tools_node = ToolNode([add_numbers])  # LangChain tool inside a graph node


def call_model(state: State) -> dict:
    response = model.invoke(state["messages"])  # LangChain model
    return {"messages": [response]}


# 3. LangGraph: ROUTING = decide what happens next (the "agent loop").
def should_continue(state: State) -> str:
    last = state["messages"][-1]
    return "tools" if last.tool_calls else END


# 4. Build the graph: START -> model -> (tools -> model loop) -> END
graph = StateGraph(State)
graph.add_node("model", call_model)
graph.add_node("tools", tools_node)
graph.add_edge(START, "model")
graph.add_conditional_edges("model", should_continue)
graph.add_edge("tools", "model")
app = graph.compile()

# 5. Run it: the model calls the tool, sees the result, and answers
result = app.invoke({"messages": [{"role": "user", "content": "What is 7 + 8? Use the tool."}]})
print(result["messages"][-1].content)
