# 🚀 PatchContext

**PatchContext** is a Retrieval-Augmented Generation (RAG) system that answers engineering questions using the development history of the FastAPI repository.

Instead of searching only documentation, PatchContext retrieves information from:

- Git Commits
- Pull Requests
- Issue Discussions

and generates grounded answers with verifiable citations to the original GitHub resources.

---

# 📌 Problem Statement

Large open-source projects contain thousands of commits, pull requests, and issue discussions.

Understanding **why** a feature was implemented or **why** a design decision was made often requires manually searching through GitHub history.

PatchContext solves this by combining semantic search with Large Language Models to provide accurate, citation-backed answers.

---

# 🎯 Objectives

- Build an end-to-end Retrieval-Augmented Generation (RAG) system.
- Index FastAPI development history.
- Retrieve relevant engineering discussions.
- Generate context-aware answers.
- Provide citations for every response.
- Reduce hallucinations using grounded retrieval.

---

# 🏗️ Architecture

```text
GitHub Repository
       │
       ▼
Commits • Pull Requests • Issues
       │
       ▼
Document Loader
       │
       ▼
Preprocessing
       │
       ▼
Chunking
       │
       ▼
Embedding Model
       │
       ▼
FAISS Vector Store
       │
       ▼
MMR Retriever
       │
       ▼
GPT-4o-mini
       │
       ▼
Answer + Citations
       │
       ▼
Streamlit UI
```

---

# 🛠️ Tech Stack

| Layer | Technology |
|--------|------------|
| Language | Python |
| API Framework | FastAPI |
| RAG Framework | LangChain |
| Vector Database | FAISS |
| Embeddings | OpenAI Embeddings |
| LLM | GPT-4o-mini |
| Frontend | Streamlit |
| Evaluation | RAGAs |

---

# 📂 Project Structure

```text
PatchContext/
│
├── app/
├── data/
├── vectorstore/
├── evaluation/
├── docs/
├── tests/
│
├── streamlit_app.py
├── requirements.txt
├── README.md
└── .env.example
```

---

# ✨ Features

- Repository-aware RAG
- Semantic Search
- Citation-based Answers
- FastAPI Backend
- Streamlit Interface
- MMR Retrieval
- Hallucination Guard
- RAGAs Evaluation

---

# 📈 Future Improvements

- Multi-repository support
- Hybrid Search (BM25 + Dense Retrieval)
- Cross-repository reasoning
- Multi-agent architecture
- Deployment on Docker and Cloud

---

# 👨‍💻 Author

**Devratan**

- PGDM (Business Analytics & Marketing)
- Lloyd Business School
- Data Scientist – Celebal Technologies

---

# 📄 License

This project is intended for educational and research purposes.
