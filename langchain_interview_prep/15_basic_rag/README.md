# 15 - Basic RAG

## What is it?

RAG (Retrieval-Augmented Generation) grounds the LLM in your own documents. First
you build an index (load, split, embed, store). At answer time you retrieve the
most relevant chunks and put them into the prompt as context.

## Flow

```
Document -> Split -> Embed -> Vector store -> Retriever
                                                  ↓ (context)
Question --------------------> Prompt -> Model -> Answer
```

## Code idea

Indexing: `TextLoader` -> `RecursiveCharacterTextSplitter` -> `FAISS`.
Querying: `retriever.invoke(question)` gives chunks, a function puts them in
`{context}`, and `prompt | model | parser` produces the grounded answer.

## Important lines

```python
retriever = vector_store.as_retriever(search_kwargs={"k": 3})
chain = get_context | prompt | model | StrOutputParser()
answer = chain.invoke(question)
```

## Interview question

1. Why use RAG instead of prompting the model directly?
2. What is the 2-phase structure of RAG?
3. What problem does chunking solve?

## Interview answer

1. The model doesn't know your private/current data; RAG gives it relevant text.
2. Indexing (load->split->embed->store) and querying (retrieve->prompt->answer).
3. Documents are too long for the context; small chunks are easier to retrieve.

## Remember

- Same embedding model for indexing and querying.
- The context in the prompt comes from the retriever, not the model.
- This is the pipeline to reproduce from memory in an interview.
