"""09 - Branching: RunnableBranch runs a runnable based on a condition.

If the question looks technical -> technical prompt.
Otherwise -> general prompt.
"""

import os

from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableBranch
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise SystemExit("Set GEMINI_API_KEY in a .env file (copy .env.example to .env)")

model = ChatGoogleGenerativeAI(
    model=os.getenv("GEMINI_MODEL", "gemini-3.5-flash"),
    api_key=api_key,
)

# 1. Two different prompts (two "branches")
technical = ChatPromptTemplate.from_messages([
    ("human", "Answer the technical question: {question}"),
])
general = ChatPromptTemplate.from_messages([
    ("human", "Answer in simple words: {question}"),
])


# 2. Condition function: decides which branch runs.
#    The input to the condition is the same dict the branch will receive.
def is_technical(input: dict) -> bool:
    keywords = ["api", "function", "database", "python", "code"]
    question = input["question"].lower()
    return any(k in question for k in keywords)


# 3. RunnableBranch: (condition, runnable_if_true, ..., runnable_if_false)
branch = RunnableBranch(
    (is_technical, technical | model),
    general | model,  # fallback when no condition matches
)

# 4. Invoke: the condition picks the right prompt automatically
answer = branch.invoke({"question": "What is a Python function?"})
print(f"Technical: {answer.content}")

answer = branch.invoke({"question": "How are you feeling today?"})
print(f"General  : {answer.content}")
