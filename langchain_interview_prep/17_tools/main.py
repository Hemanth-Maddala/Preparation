"""17 - Tools: give the model functions it can call.

The @tool decorator turns a function into a tool whose docstring and
type hints become the JSON schema. The model can then request a call.
"""

import os

from dotenv import load_dotenv
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


# 1. Define a tool with the @tool decorator
@tool
def add_numbers(a: int, b: int) -> int:
    """Add two numbers together."""
    return a + b


# 2. Inspect the tool: name, description, JSON schema
print("name       :", add_numbers.name)
print("description:", add_numbers.description)
print("args schema:", add_numbers.args_schema.model_json_schema())
print()

# 3. Invoke the tool directly, like a normal function
print("direct call:", add_numbers.invoke({"a": 2, "b": 3}))  # 5

# 4. Give the tool to the model with bind_tools.
#    The model can now DECIDE to call it; the model does NOT execute it.
model_with_tools = model.bind_tools([add_numbers])
response = model_with_tools.invoke("What is 12 + 30? Use the add_numbers tool.")

print(f"model reply type: {type(response).__name__}")  # AIMessage
print(f"tool_calls: {response.tool_calls}")

# tool_calls lists what the model WANTS to call; your code must execute them
# (an agent does this automatically - see project 18).
