# 01 - Basic model

## What is it?

The simplest LangChain program. A chat model (`ChatGoogleGenerativeAI`) wraps the
real Gemini model behind one uniform interface. You call `invoke()` with text and
get text back.

## Flow

```
User input
  ↓
Chat Model (invoke)
  ↓
Response (AIMessage)
```

## Code idea

`load_dotenv()` reads the key, `os.getenv()` never hardcodes it, the model is
created once, and `model.invoke(question)` returns an `AIMessage` whose `.content`
holds the answer.

## Important lines

```python
model = ChatGoogleGenerativeAI(model=..., api_key=api_key)
response = model.invoke(question)
answer_text = response.content
```

## Interview question

1. What does `invoke()` return?
2. Why use a ChatModel wrapper instead of the provider SDK?
3. What is the difference between `invoke`, `batch`, and `stream`?

## Interview answer

1. An `AIMessage` object; the text is in `.content`.
2. One interface for many providers (Gemini, OpenAI, Anthropic...), plus
   composability with prompts, parsers, tools, and agents.
3. `invoke` = one input, one answer; `batch` = many inputs, many answers; `stream`
   = the answer arrives token by token.

## Remember

- `model.invoke(input)` is the one method you must know.
- Result is an `AIMessage`, not a plain string.
- `.content` holds the text.
- A ChatModel is a **Runnable**, so it works with chains, streams, and batches.
