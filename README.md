# 🧠 Synera LLM Agent Challenge

This repository contains modular solutions to the Synera Agent Challenge, using LangGraph and local LLMs (e.g. via Ollama). It is organized into three progressive challenges, each showcasing document processing, retrieval, tool use, and agentic reasoning.

---

## 📁 Repository Structure

```
SYNERA_CHALLENGE/
├── challenge_1/
│   ├── agents/            # Core agent definitions
│   ├── configs/           # Configurations (e.g., model paths, agent settings)
│   ├── docs/              # Sample documents (e.g., PDFs for input)
│   ├── loaders/           # File and document loaders
│   ├── memory/            # Memory modules (e.g., vector storage, history)
│   ├── prompts/           # Prompt templates used by the agent
│   ├── tests/             # Unit and integration tests
│   ├── types/             # Type definitions and models
│   ├── agent_state.py     # State schema for LangGraph agents
│   ├── graph_config.py    # LangGraph structure and node wiring
│   └── main.py            # Entrypoint for running the agent
│
├── challenge_2/
│   └── (same structure as challenge_1, extended with more capabilities)
│
├── challenge_3/
│   ├── vectorstores/      # FAISS or other embedding store integrations
│   └── (same core structure, with additional tools and complexity)
│
├── .env                   # Environment variables (e.g., API keys)
├── .gitignore             # Ignore patterns for Git
├── README.md              # This file
└── requirements.txt       # Python dependencies
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/shayekh00/synera_challenge.git
cd synera_challenge
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Environment Variables

Create a `.env` file in each challenge folder (or at the root if shared), and add relevant API keys or config variables:

```
OLLAMA_BASE_URL=http://localhost:11434
LLM_MODEL=llama3
```

### 5. Run the Agent

```bash
cd challenge_1  # or challenge_2 / challenge_3
python main.py
```

---

## 🧪 Testing

Each challenge folder contains a `tests/` module for validating key components:

```bash
pytest tests/
```

---

## 🔍 Notes

- All challenges use [LangGraph](https://github.com/langchain-ai/langgraph) for agent orchestration.
- LLM inference is done using [Ollama](https://ollama.com/) (or compatible APIs).
- Vector search is powered by FAISS (or similar stores in `vectorstores/`).

---

## 💪 Roadmap

## 💪 Roadmap

- [x] **Challenge 1: Context-Aware Tool Invocation**  
  Extend the Synera agent to **consume a document or reference manual** before invoking tools. This mimics real engineering behavior where context (e.g., a PDF or spec) is consulted before execution. The agent must parse unstructured inputs, derive actionable context, and decide when/how to call the correct tools.

- [x] **Challenge 2: Scalable Multi-Agent Coordination**  
  Optimize communication between **multiple Synera agents** (typically 4–6 in engineering scenarios) where message history can explode. Introduce strategies for shared memory, summarized context passing, or supervised routing to maintain performance while preserving relevant context.

- [x] **Challenge 3: Complex Workflow Orchestration**  
  Enable agents to reason through **multi-step toolchains**, conditionally invoke workflows, and combine intermediate results. This includes tool routing, graph-based decisions, and modular LangGraph integration.

---

## 📜 License

MIT License. See `LICENSE` for details.
