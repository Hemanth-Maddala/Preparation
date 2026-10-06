"""15 - Basic RAG: retrieve relevant text, then let the LLM answer.

Document -> Split -> Embed -> Vector store -> Retriever -> Prompt -> Model -> Answer
"""

import os

from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise SystemExit("Set GEMINI_API_KEY in a .env file (copy .env.example to .env)")

# 1. Load + split a tiny local document
doc = TextLoader("data/company.txt").load()[0]
splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=50)
chunks = splitter.split_documents([doc])

# 2. Embed the chunks and store them
embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004", api_key=api_key)
vector_store = FAISS.from_documents(chunks, embeddings)

# 3. Create the retriever   
retriever = vector_store.as_retriever(search_kwargs={"k": 3})

# 4. Build the prompt: give the model the retrieved text as context
prompt = ChatPromptTemplate.from_messages([
    ("system", "Answer using ONLY the provided context. Say \"I don't know\" if the context has no answer."),
    ("human", "Context:\n{context}\n\nQuestion: {question}"),
])

# 5. A small function that pulls context for a question
def get_context(question: str) -> dict:
    docs = retriever.invoke(question)
    context = "\n".join(d.page_content for d in docs)
    return {"context": context, "question": question}


model = ChatGoogleGenerativeAI(
    model=os.getenv("GEMINI_MODEL", "gemini-3.5-flash"),
    api_key=api_key,
)

# 6. Chain: pull context -> fill prompt -> model -> text
chain = get_context | prompt | model | StrOutputParser()

question = "What products does the company sell?"
print(f"Q: {question}")
print(f"A: {chain.invoke(question)}")
