"""27 - RAG agent: the agent decides WHEN to retrieve.

Normal RAG:  Question -> Retriever (always) -> LLM -> Answer.
Agentic RAG: Question -> Agent decides whether retrieval is needed ->
             Retriever (tool) -> Agent -> Answer.

Here retrieval is just another tool. The agent can skip it for
questions it can answer directly.
"""

import os

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise SystemExit("Set GEMINI_API_KEY in a .env file (copy .env.example to .env)")

model = ChatGoogleGenerativeAI(
    model=os.getenv("GEMINI_MODEL", "gemini-3.5-flash"),
    api_key=api_key,
)

# 1. Build a tiny vector store
docs = [
    Document(page_content="NovaDeploy is a deployment platform for cloud apps.", metadata={"source": "products"}),
    Document(page_content="NovaMetrics is an analytics dashboard for servers.", metadata={"source": "products"}),
    Document(page_content="Gemini 3.5 is Google's flagship language model.", metadata={"source": "news"}),
]
embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004", api_key=api_key)
vector_store = FAISS.from_documents(docs, embeddings)

# 2. Retrieval is a TOOL: the agent calls it only when useful
@tool
def search_products(query: str) -> str:
    """Search the internal product catalog."""
    results = vector_store.similarity_search(query, k=2)
    return "\n".join(d.page_content for d in results)


# 3. The agent decides whether to use the tool (agentic RAG)
agent = create_agent(
    model=model,
    tools=[search_products],
    system_prompt=(
        "Use search_products when the question is about our products. "
        "Answer general questions directly without the tool."
    ),
)

for question in [
    "What does NovaDeploy do?",
    "Who won the last football world cup?",
]:
    result = agent.invoke({"messages": [{"role": "user", "content": question}]})
    print(f"Q: {question}")
    print(f"A: {result['messages'][-1].content}\n")
