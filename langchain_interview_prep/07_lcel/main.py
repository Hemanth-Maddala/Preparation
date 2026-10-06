"""07 - LCEL: LangChain Expression Language.

The `|` pipe operator passes the output of one Runnable to the next.
`prompt | model | parser` is a chain.
"""

import os

from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
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

# 1. Build each component separately
prompt = ChatPromptTemplate.from_messages([
    ("human", "Explain {topic} in one sentence."),
])
parser = StrOutputParser()

# 2. Chain them with the pipe operator
#    prompt -> model -> parser
#    Each `|` feeds the previous output into the next component.
chain = prompt | model | parser

# 3. Invoke the whole chain with the template's variables
result = chain.invoke({"topic": "LCEL"})

print(f"Result: {result}")
print(f"Type  : {type(result).__name__}")  # str
