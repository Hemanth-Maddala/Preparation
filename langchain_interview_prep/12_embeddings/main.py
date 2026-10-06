"""12 - Embeddings: turn text into a vector (a list of numbers).

Similar texts get similar vectors; the numbers capture "meaning".
"""

import os

from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise SystemExit("Set GEMINI_API_KEY in a .env file (copy .env.example to .env)")

# 1. Create the embedding model (Google's text embedding model)
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/text-embedding-004",
    api_key=api_key,
)

# 2. Embed one piece of text -> a vector (list of floats)
text = "LangChain is a framework for LLM applications."
vector = embeddings.embed_query(text)

print(f"Text   : {text}")
print(f"Vector : {vector[:5]}...")   # first 5 numbers
print(f"Length : {len(vector)}")     # number of dimensions
