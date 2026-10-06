"""19 - ReAct agent: the Reason -> Act -> Observe loop.

The agent that create_agent builds follows the ReAct pattern:
  Reason: the LLM thinks about what to do next.
  Act:    the LLM emits a tool call.
  Observe: the tool result is added to the conversation.
  (repeat until it answers directly)

This example prints every step so you can SEE the loop.
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


@tool
def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b


# 1. create_agent IS a ReAct-style agent: one tool, one loop
agent = create_agent(
    model=model,
    tools=[multiply],
    system_prompt="You are a math assistant.",
)

# 2. This task needs TWO tool calls, so the loop runs twice
result = agent.invoke({
    "messages": [{"role": "user", "content": "Compute 3 * 4, then multiply that result by 2."}],
})

# 3. Print every message to see reason -> act -> observe -> answer
for msg in result["messages"]:
    if msg.tool_calls:
        print(f"[{msg.type}] calls: {msg.tool_calls[0]['name']}{msg.tool_calls[0]['args']}")
    else:
        print(f"[{msg.type}] {msg.content}")
