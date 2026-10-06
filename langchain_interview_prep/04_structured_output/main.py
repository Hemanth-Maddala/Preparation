"""04 - Structured output: make the model return a Python object.

The model replies with JSON that Pydantic validates into a real object.
"""

import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise SystemExit("Set GEMINI_API_KEY in a .env file (copy .env.example to .env)")

model = ChatGoogleGenerativeAI(
    model=os.getenv("GEMINI_MODEL", "gemini-3.5-flash"),
    api_key=api_key,
)


# 1. Define the structure we want back, using Pydantic
class Person(BaseModel):
    name: str
    age: int


# 2. Attach the schema to the model
#    The model now promises to reply with JSON matching Person.
structured_model = model.with_structured_output(Person)

# 3. Invoke: the result is a real Person object, not text
person = structured_model.invoke(
    "Extract the person: Alice is a 30 year old engineer."
)

print(f"Type: {type(person).__name__}")  # Person
print(f"Name: {person.name}")            # Alice
print(f"Age : {person.age}")             # 30
