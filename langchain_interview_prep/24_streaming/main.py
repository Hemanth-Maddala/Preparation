"""24 - Streaming: receive output token by token instead of all at once.

invoke() = wait for the whole answer.
stream() = get chunks as they are produced (feels faster to users).
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

# --- 1. Stream a single model call ---
print("=== model.stream() ===")
for chunk in model.stream("Count from 1 to 5, one number per line."):
    print(chunk.content, end="", flush=True)
print("\n")


# --- 2. Stream an agent run ---
@tool
def add_numbers(a: int, b: int) -> int:
    """Add two numbers together."""
    return a + b


agent = create_agent(model=model, tools=[add_numbers], system_prompt="Be concise.")

print("=== agent.stream() ===")
# agent.stream() yields the agent state after each step (model/tool/answer)
for step in agent.stream({"messages": [{"role": "user", "content": "What is 2 + 2?"}]}):
    last = step.get("messages", [None])[-1]
    if last is not None:
        print(f"  [{last.type}] {last.content}")
