# 26 - SQL agent

## What is it?

An SQL agent answers natural-language questions by writing SQL, running it through
a tool, and summarizing the result. The agent decides which query to build; the
tool is read-only so nothing destructive can happen.

## Flow

```
Question
 ↓
Agent
 ↓  writes SQL
run_sql_query tool
 ↓  rows
Agent summarizes
 ↓
Answer
```

## Code idea

Create an in-memory SQLite table, expose a `run_sql_query` tool that rejects
anything not starting with SELECT, and pass it to `create_agent`. The agent
writes the SQL from the schema description in the prompt.

## Important lines

```python
@tool
def run_sql_query(query: str) -> str:
    if not query.strip().lower().startswith("select"):
        return "Only SELECT queries are allowed."
    return "\n".join(str(r) for r in DB.execute(query).fetchall())

agent = create_agent(model=model, tools=[run_sql_query], system_prompt="...")
```

## Interview question

1. How does an SQL agent work?
2. How do you keep it safe?
3. What would a production version add?

## Interview answer

1. The LLM turns the question into SQL, a tool executes it, the agent explains.
2. Read-only tool (SELECT only), restricted permissions, query validation.
3. SQLAlchemy connection management, table schema injection, query review,
   database-specific tooling.

## Remember

- The DB is a tool to the agent, not special infrastructure.
- Guard every tool you expose - the LLM will try odd queries.
- Describe the schema in the system prompt so the LLM writes correct SQL.
