# LangChain Interview Preparation Workspace

Small, clean, basic Python examples that teach **how to use LangChain**.

Goal: *understand the concept -> see the minimum code -> understand every line -> reproduce it in an interview.*

## Prerequisites

- Python 3.10+
- A Gemini API key (free): https://aistudio.google.com/apikey

## Setup

```bash
cd langchain_interview_prep
pip install -r requirements.txt

# each project reads GEMINI_API_KEY and GEMINI_MODEL from .env
copy .env.example .env
# edit .env and paste your key
```

## Layout

```
01_basic_model         model + invoke()
02_messages            System/Human/AI messages
03_prompt_template     ChatPromptTemplate with variables
04_structured_output   Pydantic + with_structured_output
05_basic_chain         prompt -> model -> parser
06_runnable            invoke / batch / stream
07_lcel                the `|` pipe operator
08_parallel            RunnableParallel
09_branching           RunnableBranch
10_document_loader     TextLoader -> Document
11_text_splitter       RecursiveCharacterTextSplitter
12_embeddings          text -> vector
13_vector_store        FAISS store + similarity_search
14_retriever           vector_store.as_retriever()
15_basic_rag           load -> split -> embed -> store -> retrieve -> answer
16_advanced_rag        query rewriting / metadata filter / rerank idea
17_tools               @tool, schema, bind_tools
18_basic_agent         create_agent
19_react_agent         Reason -> Act -> Observe loop
20_structured_agent    create_agent + response_format (Pydantic)
21_memory              checkpointer + threads
22_middleware          before/after model hooks
23_human_in_the_loop   interrupt + approve/resume
24_streaming           model.stream() + agent.stream()
25_async               ainvoke / astream / abatch
26_sql_agent           safe read-only SQLite agent
27_rag_agent           agent decides when to retrieve
28_multi_tool_agent    LLM picks the right tool
29_multi_agent         supervisor -> research -> writer
30_langchain_langgraph LangChain components in a StateGraph
```

## How to study

1. Read `LANGCHAIN_LEARNING_ROADMAP.txt` for the order.
2. For each project: read `README.md`, then `python main.py`, then read the code line by line.
3. Cover `main.py` and try to rewrite it from memory.
4. Finish with `LANGCHAIN_INTERVIEW_PREPARATION.txt`.

## Environment variables

| Variable        | Meaning                                     | Used by           |
|-----------------|---------------------------------------------|-------------------|
| `GEMINI_API_KEY`| Google AI Studio API key                    | every LLM example |
| `GEMINI_MODEL`  | Model id, default `gemini-3.5-flash`        | every LLM example |

Never hardcode keys. All examples load them with `os.getenv()`.

## Validation

`LANGCHAIN_VALIDATION_REPORT.txt` describes what was checked for every project.
