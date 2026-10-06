"""21 - Memory: keep conversation context with a checkpointer and threads.

Checkpointer = saves the state of every run (a store).
Thread       = one conversation. Reusing the same thread_id means
               the agent remembers earlier turns.
"""

import os

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.checkpoint.memory import InMemorySaver

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


# 1. Checkpointer saves conversation state; threads separate conversations
agent = create_agent(
    model=model,
    tools=[add_numbers],
    system_prompt="You are a helpful assistant.",
    checkpointer=InMemorySaver(),
)

config = {"configurable": {"thread_id": "conversation-1"}}

# 2. First turn
result = agent.invoke(
    {"messages": [{"role": "user", "content": "My name is Alice."}]},
    config=config,
)
print("Turn 1:", result["messages"][-1].content)

# 3. Second turn with the SAME thread_id: the agent remembers turn 1
result = agent.invoke(
    {"messages": [{"role": "user", "content": "What is my name?"}]},
    config=config,
)
print("Turn 2:", result["messages"][-1].content)
