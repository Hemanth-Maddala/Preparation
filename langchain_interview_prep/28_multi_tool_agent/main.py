"""28 - Multi-tool agent: the LLM picks the right tool for the question.

Three small tools: calculator, weather (mock), today's date.
The main point: the LLM CHOOSES which tool (if any) fits the question.
"""

import os
from datetime import date

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
def calculator(expression: str) -> str:
    """Evaluate a simple arithmetic expression like '2 + 3 * 4'."""
    return str(eval(expression))  # demo only; never use eval() in production


@tool
def get_weather(city: str) -> str:
    """Get the current weather for a city (mock)."""
    return f"It is 22C and sunny in {city}."


@tool
def today() -> str:
    """Get today's date."""
    return date.today().isoformat()


# 1. Give the agent all three tools; it chooses which one fits
agent = create_agent(
    model=model,
    tools=[calculator, get_weather, today],
    system_prompt="Use the right tool for each question.",
)

for question in [
    "What is 6 * 7?",
    "What is the weather in Paris?",
    "What is today's date?",
]:
    result = agent.invoke({"messages": [{"role": "user", "content": question}]})
    print(f"Q: {question}")
    print(f"A: {result['messages'][-1].content}\n")
