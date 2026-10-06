"""08 - RunnableParallel: run several branches at the same time.

One input feeds two independent branches; the results come back as a dict.
"""

import os

from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise SystemExit("Set GEMINI_API_KEY in a .env file (copy .env.example to .env)")

model = ChatGoogleGenerativeAI(
    model=os.getenv("GEMINI_MODEL", "gemini-3.5-flash"),
    api_key=api_key,
)

# 1. Two prompt templates, both using the {topic} variable
summary_prompt = ChatPromptTemplate.from_messages([
    ("human", "Summarize {topic} in one sentence."),
])
keywords_prompt = ChatPromptTemplate.from_messages([
    ("human", "List 3 keywords for {topic}, separated by commas."),
])

# 2. RunnableParallel runs both branches with the same input
parallel = RunnableParallel(
    summary=summary_prompt | model,
    keywords=keywords_prompt | model,
)

# 3. Invoke once: the result is a dict with one key per branch
result = parallel.invoke({"topic": "LangChain"})

print(f"Summary : {result['summary'].content}")
print(f"Keywords: {result['keywords'].content}")
