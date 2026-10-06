"""20 - Structured agent: an agent that returns a validated Pydantic object."""

import os

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel

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


# 1. Define the structured answer the agent must produce
class Answer(BaseModel):
    answer: str
    confidence: float


# 2. Pass response_format to create_agent (same idea as with_structured_output)
agent = create_agent(
    model=model,
    tools=[add_numbers],
    system_prompt="You are a helpful assistant.",
    response_format=Answer,
)

result = agent.invoke({
    "messages": [{"role": "user", "content": "What is 3 + 4?"}],
})

# 3. structured_response holds the validated Pydantic object
answer = result["structured_response"]
print(f"Type       : {type(answer).__name__}")  # Answer
print(f"answer     : {answer.answer}")
print(f"confidence : {answer.confidence}")
