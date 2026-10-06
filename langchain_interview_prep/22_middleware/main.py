"""22 - Middleware: hooks that run around the agent's model calls.

This example logs what happens before and after the model is called.
The same mechanism can add retries, guardrails, or modifications.
"""

import os

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.agents.middleware import AgentMiddleware
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
def add_numbers(a: int, b: int) -> int:
    """Add two numbers together."""
    return a + b


# 1. Middleware = code that wraps agent steps.
#    Subclass AgentMiddleware and override the hooks you need.
class LoggingMiddleware(AgentMiddleware):
    def before_model(self, state, runtime):
        last = state["messages"][-1]
        print(f"   [before_model] last message: {last.content[:50]}")
        return None  # returning a dict would update the agent state

    def after_model(self, state, runtime):
        print("   [after_model] model call finished")
        return None


# 2. Pass middleware to create_agent
agent = create_agent(
    model=model,
    tools=[add_numbers],
    system_prompt="You are a helpful assistant.",
    middleware=[LoggingMiddleware()],
)

print("Running the agent...")
result = agent.invoke({
    "messages": [{"role": "user", "content": "What is 10 + 5?"}],
})
print(f"Answer: {result['messages'][-1].content}")

# Other useful hooks (not shown to keep this small):
#   wrap_model_call(...)  -> intercept/model calls (retries, fallbacks)
#   wrap_tool_call(...)   -> tool middleware (logging, approvals)
# Built-ins exist too: PIIMiddleware, ModelRetryMiddleware, ToolRetryMiddleware...
