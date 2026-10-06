"""26 - SQL agent: an agent that answers questions by querying SQLite.

Question -> Agent -> writes SQL -> run_sql_query tool -> result -> answer.

The tool only allows SELECT, so destructive queries are impossible here.
"""

import os
import sqlite3

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise SystemExit("Set GEMINI_API_KEY in a .env file (copy .env.example to .env)")

model = ChatGoogleGenerativeAI(
    model=os.getenv("GEMINI_MODEL", "gemini-3.5-flash"),
    api_key=api_key,
)


# 1. Create a tiny in-memory SQLite table with a few rows
def create_db() -> sqlite3.Connection:
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE employees (name TEXT, department TEXT, salary INT)")
    conn.executemany(
        "INSERT INTO employees VALUES (?, ?, ?)",
        [("Alice", "Engineering", 120000),
         ("Bob", "Sales", 80000),
         ("Carol", "Engineering", 95000)],
    )
    return conn


DB = create_db()


# 2. A safe SQL tool: only SELECT queries are allowed
@tool
def run_sql_query(query: str) -> str:
    """Run a READ-ONLY SQL query and return the results as text."""
    if not query.strip().lower().startswith("select"):
        return "Only SELECT queries are allowed."
    rows = DB.execute(query).fetchall()
    return "\n".join(str(r) for r in rows)


# 3. Give the agent the SQL tool; it writes the SQL itself
agent = create_agent(
    model=model,
    tools=[run_sql_query],
    system_prompt="Answer questions by writing SQL. Use the tool, then summarize the result.",
)

result = agent.invoke({
    "messages": [{"role": "user", "content": "Which department has the highest total salary?"}],
})
print(result["messages"][-1].content)
