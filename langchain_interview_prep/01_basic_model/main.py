"""01 - Basic model: the simplest LangChain program.

Flow: user input -> Chat Model -> response
"""

import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

# 1. Load the API key from the environment (never hardcode it)
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise SystemExit("Set GEMINI_API_KEY in a .env file (copy .env.example to .env)")

# 2. Create the model
#    ChatGoogleGenerativeAI wraps the real Gemini model behind
#    LangChain's uniform ChatModel interface.
model = ChatGoogleGenerativeAI(
    model=os.getenv("GEMINI_MODEL", "gemini-3.5-flash"),
    api_key=api_key,
)

# 3. Invoke the model: one input in, one answer out
question = "Explain in one sentence what a large language model is."

# invoke() returns an AIMessage object; the text is in .content
response = model.invoke(question)

print(f"Question   : {question}")
print(f"Answer     : {response.content}")
print(f"Return type: {type(response).__name__}")  # AIMessage
