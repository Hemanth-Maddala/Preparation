"""
STEP 15: SOLUTIONS
==================
Solutions for all 15 tasks.
Try to solve them first before looking here.
"""

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough


def format_docs(docs):
    return "\n\n".join(d.page_content for d in docs)


# ============================================
# LEVEL 1: Solutions
# ============================================

def task_1():
    """Load a document"""
    loader = TextLoader("data/sample.txt", encoding="utf-8")
    docs = loader.load()
    print(f"Number of documents: {len(docs)}")
    return docs


def task_2():
    """Split into chunks"""
    docs = task_1()
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=300, chunk_overlap=30
    )
    chunks = splitter.split_documents(docs)
    print(f"Number of chunks: {len(chunks)}")
    return chunks


def task_3():
    """Create embeddings"""
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    embedding = embeddings.embed_query("Acme was founded in 1985")
    print(f"Embedding dimension: {len(embedding)}")
    return embeddings


def task_4():
    """Create Chroma store"""
    chunks = task_2()
    embeddings = task_3()
    vectorstore = Chroma.from_documents(chunks, embeddings)
    print(f"Documents in store: {vectorstore._collection.count()}")
    return vectorstore


def task_5():
    """Similarity search"""
    vectorstore = task_4()
    results = vectorstore.similarity_search("When was Acme founded?", k=2)
    for i, doc in enumerate(results):
        print(f"\nResult {i+1}: {doc.page_content[:100]}...")
    return results


# ============================================
# LEVEL 2: Solutions
# ============================================

def task_6():
    """Create a retriever"""
    vectorstore = task_4()
    retriever = vectorstore.as_retriever(search_kwargs={"k": 2})
    docs = retriever.invoke("What products does Acme sell?")
    print(f"Retrieved {len(docs)} documents")
    for doc in docs:
        print(f"- {doc.page_content[:100]}...")
    return retriever


def task_7():
    """Add an LLM"""
    llm = ChatOllama(model="tinyllama", temperature=0.3)
    response = llm.invoke("What is 2+2?")
    print(f"Answer: {response.content}")
    return llm


def task_8():
    """Create a RAG prompt"""
    prompt = ChatPromptTemplate.from_template(
        "Answer based on context:\n{context}\n\nQuestion: {question}\n\nAnswer:"
    )
    print(f"Input variables: {prompt.input_variables}")
    return prompt


def task_9():
    """Connect retriever + LLM"""
    vectorstore = task_4()
    retriever = vectorstore.as_retriever(search_kwargs={"k": 2})
    llm = ChatOllama(model="tinyllama", temperature=0.3)
    prompt = ChatPromptTemplate.from_template(
        "Answer based on context:\n{context}\n\nQuestion: {question}\n\nAnswer:"
    )
    
    chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt | llm | StrOutputParser()
    )
    
    answer = chain.invoke("When was Acme founded?")
    print(f"Answer: {answer}")
    return chain


def task_10():
    """Return source documents"""
    vectorstore = task_4()
    retriever = vectorstore.as_retriever(search_kwargs={"k": 2})
    llm = ChatOllama(model="tinyllama", temperature=0.3)
    prompt = ChatPromptTemplate.from_template(
        "Answer based on context:\n{context}\n\nQuestion: {question}\n\nAnswer:"
    )
    
    def rag_with_sources(question):
        docs = retriever.invoke(question)
        context = format_docs(docs)
        formatted_prompt = prompt.invoke({"context": context, "question": question})
        response = llm.invoke(formatted_prompt)
        return {
            "answer": response.content,
            "sources": [d.page_content[:100] for d in docs]
        }
    
    result = rag_with_sources("When was Acme founded?")
    print(f"Answer: {result['answer']}")
    print(f"Sources: {len(result['sources'])}")
    return result


# ============================================
# LEVEL 3: Solutions
# ============================================

def task_11():
    """Add metadata filtering"""
    vectorstore = task_4()
    results = vectorstore.similarity_search(
        "When was Acme founded?",
        k=2,
        filter={"source": "data/sample.txt"}
    )
    print(f"Filtered results: {len(results)}")
    return results


def task_12():
    """Change top-k"""
    vectorstore = task_4()
    
    for k in [1, 3, 5]:
        results = vectorstore.similarity_search("Acme", k=k)
        print(f"k={k}: {len(results)} results")


def task_13():
    """Handle no relevant documents"""
    vectorstore = task_4()
    retriever = vectorstore.as_retriever(search_kwargs={"k": 2})
    llm = ChatOllama(model="tinyllama", temperature=0.3)
    prompt = ChatPromptTemplate.from_template(
        "Answer based on context:\n{context}\n\nQuestion: {question}\n\nAnswer:"
    )
    
    def safe_rag(question):
        docs = retriever.invoke(question)
        if not docs:
            return "No relevant information found."
        context = format_docs(docs)
        formatted_prompt = prompt.invoke({"context": context, "question": question})
        response = llm.invoke(formatted_prompt)
        return response.content
    
    # Test with unrelated question
    answer = safe_rag("What is the meaning of life?")
    print(f"Answer: {answer}")


def task_14():
    """Add conversation history"""
    vectorstore = task_4()
    retriever = vectorstore.as_retriever(search_kwargs={"k": 2})
    llm = ChatOllama(model="tinyllama", temperature=0.3)
    
    prompt = ChatPromptTemplate.from_template(
        """Answer based on context. Use conversation history for follow-up questions.

Context: {context}

History: {history}

Question: {question}

Answer:"""
    )
    
    def rag_with_history(question, history=""):
        docs = retriever.invoke(question)
        context = format_docs(docs)
        formatted_prompt = prompt.invoke({
            "context": context,
            "history": history,
            "question": question
        })
        response = llm.invoke(formatted_prompt)
        return response.content
    
    # Test with 2 questions
    q1 = "When was Acme founded?"
    a1 = rag_with_history(q1)
    print(f"Q1: {q1}")
    print(f"A1: {a1}\n")
    
    history = f"Q: {q1}\nA: {a1}"
    q2 = "Who is the CEO?"
    a2 = rag_with_history(q2, history)
    print(f"Q2: {q2}")
    print(f"A2: {a2}")


def task_15():
    """Convert to FastAPI endpoint"""
    from fastapi import FastAPI
    from pydantic import BaseModel
    import uvicorn
    
    app = FastAPI()
    
    # Build RAG chain (reuse from task_9)
    vectorstore = task_4()
    retriever = vectorstore.as_retriever(search_kwargs={"k": 2})
    llm = ChatOllama(model="tinyllama", temperature=0.3)
    prompt = ChatPromptTemplate.from_template(
        "Answer based on context:\n{context}\n\nQuestion: {question}\n\nAnswer:"
    )
    
    chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt | llm | StrOutputParser()
    )
    
    class QuestionRequest(BaseModel):
        question: str
    
    @app.post("/ask")
    def ask(request: QuestionRequest):
        docs = retriever.invoke(request.question)
        context = format_docs(docs)
        answer = chain.invoke(request.question)
        return {
            "answer": answer,
            "sources": [d.page_content[:100] for d in docs]
        }
    
    print("FastAPI app created. Run with: uvicorn practice_solutions:app --reload")
    return app


if __name__ == "__main__":
    print("Running Task 1...")
    task_1()
    
    print("\nRunning Task 5...")
    task_5()
    
    print("\nRunning Task 9...")
    task_9()