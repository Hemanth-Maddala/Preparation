"""29 - Multi-agent: a supervisor routes work to specialist agents.

User -> Supervisor (decides who handles it)
          -> Research Agent (collects facts) -> Writer Agent (turns facts into text)
          -> Writer Agent (direct)
Each agent is just a small function using the same real Gemini model.
"""

import os

from dotenv import load_dotenv
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


# Agent 1: collects facts about a topic
def research_agent(question: str) -> str:
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a research specialist. List facts about the topic."),
        ("human", "{question}"),
    ])
    return (prompt | model).invoke({"question": question}).content


# Agent 2: turns facts (or a prompt) into a readable article
def writer_agent(facts: str) -> str:
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a writer. Turn the facts into 3 short paragraphs."),
        ("human", "Facts:\n{facts}"),
    ])
    return (prompt | model).invoke({"facts": facts}).content


# Supervisor: decides which agent(s) handle the request
def supervisor(question: str) -> str:
    prompt = ChatPromptTemplate.from_messages([
        ("system", "Decide if the user asks for RESEARCH (facts) or WRITING (create text). "
                   "Reply with exactly one word: RESEARCH or WRITE."),
        ("human", "{question}"),
    ])
    decision = (prompt | model).invoke({"question": question}).content.strip().upper()

    if "RESEARCH" in decision:
        # research first, then the writer turns the facts into an answer
        return writer_agent(research_agent(question))
    return writer_agent(question)


print(supervisor("What is a large language model?"))
