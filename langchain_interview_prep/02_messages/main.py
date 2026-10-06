"""02 - Messages: how LangChain represents a conversation.

Each message has a role (system / human / ai). The model reads the
whole list of messages as one conversation.
"""

import os

from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise SystemExit("Set GEMINI_API_KEY in a .env file (copy .env.example to .env)")

model = ChatGoogleGenerativeAI(
    model=os.getenv("GEMINI_MODEL", "gemini-3.5-flash"),
    api_key=api_key,
)

# 1. Build a tiny conversation as a list of messages
messages = [
    SystemMessage("You are a helpful assistant that answers in one sentence."),
    HumanMessage("What is LangChain?"),
]

# 2. Send the whole conversation to the model
response = model.invoke(messages)

print(f"Answer: {response.content}")
print()

# 3. The three message classes (no memory system needed here)
#    SystemMessage sets behaviour, HumanMessage is the user, AIMessage is the model.
print(f"SystemMessage = assistant behaviour")
print(f"HumanMessage  = user input")
print(f"AIMessage     = model output (this response is a {type(response).__name__})")
print(f"response.role = {response.role}")  # 'ai'
print()

# 4. AI messages can be fed back in to continue the conversation
conversation = messages + [response, HumanMessage("Give a one-line example.")]
next_response = model.invoke(conversation)
print(f"Next turn: {next_response.content}")
