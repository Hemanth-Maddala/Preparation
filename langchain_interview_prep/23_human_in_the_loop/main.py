"""23 - Human in the loop: pause an agent until a human approves.

The agent runs until it wants to call a tool. The run pauses there.
A human decides: approve (Command(resume=True)) or reject.
"""

import os

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.types import Command

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise SystemExit("Set GEMINI_API_KEY in a .env file (copy .env.example to .env)")

model = ChatGoogleGenerativeAI(
    model=os.getenv("GEMINI_MODEL", "gemini-3.5-flash"),
    api_key=api_key,
)


@tool
def charge_card(amount: int) -> str:
    """Charge a credit card (sensitive operation)."""
    return f"Charged {amount}."


# 1. interrupt_before=["tools"]: pause BEFORE any tool executes.
#    A checkpointer is required so the run can be resumed later.
agent = create_agent(
    model=model,
    tools=[charge_card],
    system_prompt="You are a billing assistant.",
    checkpointer=InMemorySaver(),
    interrupt_before=["tools"],
)

config = {"configurable": {"thread_id": "payment-1"}}

# 2. First invoke: the agent reaches the tool and pauses
result = agent.invoke(
    {"messages": [{"role": "user", "content": "Charge my card 50 dollars."}]},
    config=config,
)

# 3. The run came back paused right before the tool ran.
#    (Note: interrupt_before stops BEFORE the node, so no "__interrupt__"
#    key appears in the result - the Interrupt list only shows up when you
#    call interrupt() inside a node yourself.)

# 4. A human approves -> resume with Command(resume=True)
#    (resume=False would reject and stop the run)
result = agent.invoke(Command(resume=True), config=config)
print("Tool executed:", result["messages"][-1].content)
