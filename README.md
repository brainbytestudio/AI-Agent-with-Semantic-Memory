# 🧠AI-Agent-with-Semantic-Memory
 
### Production-Ready AI Agent with Gemini, ChromaDB & Async Tool Calling

A production-style AI Agent that combines:

- 🔍 Semantic Long-Term Memory (Vector DB)
- 🌐 Async Web Search Tool
- 🤖 Gemini as Execution LLM
- 🧠 Intelligent Tool-Calling Architecture
- 📊 Phoenix Tracing for Observability
- 💬 Gradio UI for Interaction

Unlike traditional chatbots that rely only on chat history, this system remembers information **by meaning**, not keywords.

---

## 🚀 Demo Architecture

User Query
↓
Semantic Memory Search (ChromaDB)
↓
Relevant Found? ── Yes ──► Reuse Memory
│
No
↓
Async Web Search
↓
Gemini Generates Final Answer
↓
Store Clean Knowledge in Vector DB


Each message:
- Runs as a separate trace
- Grouped by conversation_id
- Fully observable via Phoenix

---

## 📥 Installation Guide

### 1️⃣ Install `uv` (Package Manager)

`uv` is a modern, ultra-fast Python package manager written in **Rust**.

#### Windows (PowerShell)

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

#### macOS / Linux (Terminal)

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

> 💡 macOS users can also install via Homebrew:

```bash
brew install uv
```

---

### 2️⃣ Setup Project & Dependencies

Clone the repository and install all required dependencies using `uv`:

```bash
# Create a virtual environment
uv venv

# Install project dependencies
uv pip install --
```

---

## 🔐 Environment Variables (.env)

Create a `.env` file in the project root and add your API keys:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

> 🔒 These keys are loaded securely using `python-dotenv` and are **never hard-coded**.

---

## 🏗 Project Structure
AI_Memory_Agent/
│
├── src/
│ ├── app.py # Orchestrator + Gradio UI
│ ├── my_agents.py # Agent Definition & Prompting
│ └── tools/
│ ├── search.py # Async Web Search Tool
│ └── vector_ops.py # Semantic Memory Layer
│
├── conversation_memory/ # ChromaDB Persistent Storage
├── .env # API Keys (Not committed)
├── .gitignore
└── README.md


---

## 🧠 Core Concepts Implemented

### 1️⃣ Semantic Memory
- Sentence Transformers for embeddings
- ChromaDB for persistent vector storage
- Meaning-based similarity search
- Timestamp-aware reasoning

---

### 2️⃣ Agent Tool Calling
- OpenAI Agents SDK
- Structured function tools
- LLM decides when to:
  - Call memory
  - Call web search
  - Generate final answer

---

### 3️⃣ Async Execution
- Async web search using `asyncio.gather`
- Parallel search queries
- Non-blocking tool execution

---

### 4️⃣ Observability (Phoenix)
- Auto-instrumented tracing
- Separate trace per user message
- Grouped via `conversation_id`
- Production-style debugging

---

## 🛠 Tech Stack

| Component | Technology |
|-----------|------------|
| LLM | Gemini (OpenAI-Compatible API) |
| Agent Framework | OpenAI Agents SDK |
| Vector Database | ChromaDB |
| Embeddings | SentenceTransformers (all-MiniLM-L6-v2) |
| Async Execution | asyncio |
| Tracing | Arize Phoenix |
| UI | Gradio |

---

## 🔧 Setup Instructions

### 1️⃣ Clone the repository

```bash
git clone https://github.com/yourusername/AI-Agent-with-Semantic-Memory.git
cd AI-Agent-with-Semantic-Memory

⭐ If You Found This Useful

Give this repo a star ⭐
Follow for more advanced AI system builds 🚀
