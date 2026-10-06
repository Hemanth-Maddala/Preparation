"""03 - Prompt template: a reusable prompt with variables.

Template -> fill in {topic} -> messages -> model
"""

import os

from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise SystemExit("Set GEMINI_API_KEY in a .env file (copy .env.example to .env)")

model = ChatGoogleGenerativeAI(
    model=os.getenv("GEMINI_MODEL", "gemini-3.5-flash"),
    api_key=api_key,
)

# 1. Create the prompt template with one variable: {topic}
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a friendly teacher."),
    ("human", "What is {topic}?"),
])

# 2. Fill in the variable -> the template becomes a list of messages
messages = prompt.invoke({"topic": "RAG"})
print(messages.to_messages())  # [SystemMessage, HumanMessage("What is RAG?")]

# 3. Connect the prompt to the model with the pipe operator (LCEL)
chain = prompt | model

# 4. Invoke the chain: the template variable is the input
answer = chain.invoke({"topic": "RAG"})
print(f"Answer: {answer.content}")
