# 04 - Structured output

## What is it?

`with_structured_output(Schema)` makes the model return data that matches a
Pydantic model. Instead of parsing free text, you get a validated Python object.

## Flow

```
Pydantic schema (Person)
  ↓
model.with_structured_output(Person)
  ↓
User text
  ↓
Person object (validated)
```

## Code idea

Define a `BaseModel` class, pass the class to `with_structured_output`, then
`invoke()` returns an instance of that class. Access fields with dot notation.

## Important lines

```python
class Person(BaseModel):
    name: str
    age: int

structured_model = model.with_structured_output(Person)
person = structured_model.invoke("Alice is a 30 year old engineer.")
person.name   # "Alice"
```

## Interview question

1. What does `with_structured_output` do?
2. Why use Pydantic for LLM output?
3. What happens if the model returns invalid data?

## Interview answer

1. It attaches a schema so the model answers with matching JSON, which LangChain
   validates into a Pydantic object.
2. Guaranteed types, autocomplete, validation errors instead of parsing bugs.
3. Pydantic raises a validation error rather than returning broken data.

## Remember

- The schema is a normal `BaseModel` class.
- Result is an object, not a dict or string.
- Works for agents too (see project 20: `create_agent(response_format=...)`).
