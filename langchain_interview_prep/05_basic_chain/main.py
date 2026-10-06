"""05 - Basic chain: prompt -> model -> parser.

A chain is just components connected together so the output of one
becomes the input of the next.
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

# 1. Create the prompt
prompt = ChatPromptTemplate.from_messages([
    ("human", "Translate this to English: {text}"),
])

# 2. Create the parser: turns the AIMessage into a plain string
parser = StrOutputParser()

# 3. Build the chain with the pipe operator
chain = prompt | model | parser

# 4. Invoke the chain with the template variable
result = chain.invoke({"text": "Bonjour, comment allez-vous?"})

print(f"Result: {result}")
print(f"Type  : {type(result).__name__}")  # str, thanks to the parser
