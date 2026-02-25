import os
from dotenv import load_dotenv
from datetime import datetime
from agents import Agent, OpenAIChatCompletionsModel
from openai import AsyncOpenAI

from tools.vector_ops import semantic_memory_search
from tools.search import multi_web_search

load_dotenv()

# -------------------------------
# Gemini (Execution LLM)
# -------------------------------
client = AsyncOpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=client
)

memory_chatbot = Agent(
    name="SemanticBrain",
    model=model,
    instructions=f"""
You are a professional AI assistant with semantic long-term memory.
Current date and time: {datetime.now().isoformat()}.

CORE BEHAVIOR:
1. ALWAYS call `semantic_memory_search` first.
2. Evaluate returned knowledge by:
   - semantic relevance
   - timestamp
   - topic stability
3. Decide whether memory is sufficient or a web search is justified.
4. Prefer memory reuse whenever reasonable.
5. Use web search ONLY when:
   - no relevant memory exists, or
   - the topic likely changes over time.

RESPONSE RULES:
- If using memory, acknowledge it naturally ("As I remember…").
- If using web search, imply freshness.
- Do NOT expose chain-of-thought.
- Be clear, friendly, and factual.
""",
    tools=[semantic_memory_search, multi_web_search],
)
