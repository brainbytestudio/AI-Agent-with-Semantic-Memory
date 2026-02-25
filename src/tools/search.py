import asyncio
from ddgs import DDGS
from agents import function_tool

@function_tool
async def multi_web_search(queries: list[str]) -> str:
    """Performs multiple searches simultaneously for deep research."""
    async def fetch(q):
        with DDGS() as ddgs:
            results = list(ddgs.text(q, max_results=3))
            return f"Query: {q}\n" + "\n".join([r['body'] for r in results])

    tasks = [fetch(query) for query in queries]
    results = await asyncio.gather(*tasks)
    return "\n\n---\n\n".join(results)