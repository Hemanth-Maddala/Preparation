# 27 - RAG agent

## What is it?

Agentic RAG makes retrieval a TOOL the agent chooses to use. Normal RAG always
retrieves; agentic RAG retrieves only when the question needs your documents.

## Flow

```
Normal RAG:  Question -> Retriever (always) -> LLM -> Answer
Agentic RAG: Question -> Agent decides
                          ├── needs docs  -> search_products tool -> answer
                          └── general     -> answer directly
```

## Code idea

The vector store is wrapped in a `@tool`. The system prompt tells the agent when
to use it. This is just an agent with a retrieval tool.

## Important lines

```python
@tool
def search_products(query: str) -> str:
    return "\n".join(d.page_content for d in vector_store.similarity_search(query, k=2))

agent = create_agent(model=model, tools=[search_products], system_prompt="...")
```

## Interview question

1. Normal RAG vs agentic RAG?
2. Why is agentic RAG better sometimes?
3. How is retrieval represented in an agent?

## Interview answer

1. Normal RAG always retrieves; agentic RAG has an agent decide whether to
   retrieve (and can chain searches).
2. Fewer useless retrievals, can refine queries, combines retrieval with other
   tools (SQL, web).
3. As a tool - the agent calls it like any other function.

## Remember

- Agentic RAG = agent + retrieval tool, not special code.
- The system prompt controls when the tool is used.
- Good for "sometimes grounded, sometimes general" assistants.
