"""18 - Basic agent: an LLM that decides when to call a tool.

Model call  = ask the LLM, get text.
Chain       = fixed pipeline (prompt -> model -> parser).
Agent       = loop: LLM decides -> maybe calls a tool -> repeats -> final answer.

create_agent is the CURRENT high-level agent API. Under the hood it is a
LangGraph loop, but you don't need to build the graph yourself.
"""

import os

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise SystemExit("Set GEMINI_API_KEY in a .env file (copy .env.example to .env)")

model = ChatGoogleGenerativeAI(
    model=os.getenv("GEMINI_MODEL", "gemini-3.5-flash"),
    api_key=api_key,
)


# 1. Create two simple tools
@tool
def add_numbers(a: int, b: int) -> int:
    """Add two numbers together."""
    return a + b


@tool
def get_weather(city: str) -> str:
    """Get the current weather for a city (mock)."""
    return f"It is sunny in {city}."


# 2. Create the agent: model + tools + system prompt
agent = create_agent(
    model=model,
    tools=[add_numbers, get_weather],
    system_prompt="You are a helpful assistant. Use tools when needed.",
)

# 3. Invoke with a list of messages
result = agent.invoke({
    "messages": [{"role": "user", "content": "What is 5 + 7?"}],
})

# 4. The last message is the final answer
answer = result["messages"][-1]
print(f"Final answer: {answer.content}")
