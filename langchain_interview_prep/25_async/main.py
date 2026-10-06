"""25 - Async: run LLM calls without blocking, so many can happen at once.

Sync:    invoke / batch / stream
Async:   ainvoke / abatch / astream   (an 'a' prefix = async version)
"""

import asyncio
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

prompt = ChatPromptTemplate.from_messages([("human", "Say {word} in one word.")])
chain = prompt | model


async def main():
    # 1. ainvoke(): async version of invoke()
    one = await chain.ainvoke({"word": "hello"})
    print("ainvoke :", one.content)

    # 2. abatch(): async version of batch()
    many = await chain.abatch([{"word": "hello"}, {"word": "bye"}])
    print("abatch  :", [m.content for m in many])

    # 3. astream(): async version of stream()
    print("astream :", end=" ")
    async for chunk in chain.astream({"word": "hello"}):
        print(chunk.content, end="", flush=True)
    print()

    # 4. Why async matters: run several calls concurrently
    results = await asyncio.gather(
        chain.ainvoke({"word": "one"}),
        chain.ainvoke({"word": "two"}),
        chain.ainvoke({"word": "three"}),
    )
    print("gather  :", [r.content for r in results])


asyncio.run(main())
