# Adaptive AI Agent

A personalized AI assistant built with LangChain, LangGraph and Streamlit.

The assistant combines personalized prompting, conversation memory and
Retrieval-Augmented Generation (RAG) to answer questions using user-provided
documents.

---

# 🚀 Features

## ✅ Implemented

- Personalized user profile
- Dynamic system prompt
- LangChain LCEL pipeline
- LangGraph-based conversation flow
- Streaming responses
- Multi-conversation chat
- Automatic conversation titles
- Conversation memory
- PDF, TXT and Markdown document ingestion
- Recursive document chunking
- HuggingFace embeddings
- Chroma vector database
- BM25 lexical retrieval
- Hybrid retrieval
- MMR vector retrieval
- RAG-based question answering
- Retrieved source display
- User document upload and indexing
- Configurable LLM backend with Groq

---

# 🛣 Roadmap

## Sprint 0 — Project Setup

- [x] Repository
- [x] Python environment
- [x] Project architecture
- [x] Streamlit application

---

## Sprint 1 — Personalized Chat

- [x] User profile
- [x] Dynamic prompt generation
- [x] LangChain LCEL
- [x] Conversation memory
- [x] Chat interface

---

## Sprint 2 — Better Chat Experience

- [x] Streaming responses
- [x] Multi-conversation
- [x] Automatic conversation titles
- [ ] Conversation persistence
- [ ] Chat export
- [ ] Conversation rename
- [ ] Conversation delete

---

## Sprint 3 — Retrieval-Augmented Generation (RAG)

- [x] PDF loader
- [x] URL loader
- [x] Markdown loader
- [x] Recursive chunking
- [x] HuggingFace embeddings
- [x] ChromaDB
- [x] BM25 retrieval
- [x] Hybrid retrieval
- [x] MMR retrieval
- [x] History-aware retrieval
- [x] Retrieval chain
- [x] Source citations
- [x] User document upload and indexing

---

## Sprint 4 — Agent & Tools

- [ ] Tool calling
- [ ] Calculator tool
- [ ] Web search tool
- [ ] Structured outputs
- [ ] Pydantic schemas
- [ ] RunnableBranch
- [ ] RunnableParallel
- [ ] RunnablePassthrough

---

## Sprint 5 — Adaptive Middleware

- [ ] Intent classification
- [ ] Dynamic prompt adaptation
- [ ] Dynamic tool routing
- [ ] Context optimization
- [ ] Configurable models
- [ ] Message trimming

---

## Sprint 6 — Polish

- [ ] Agent Inspector
- [ ] Prompt viewer
- [ ] Token usage
- [ ] Latency metrics
- [ ] Tool execution trace
- [ ] Docker
- [ ] Streamlit Cloud
- [ ] Screenshots

---

# 🏗️ Architecture

```text
                    ┌─────────────────────┐
                    │      Streamlit      │
                    │        UI           │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Conversation      │
                    │     Manager          │
                    └──────────┬──────────┘
                               │
                    ┌──────────▼──────────┐
                    │    LangGraph /      │
                    │    LangChain        │
                    └──────────┬──────────┘
                               │
                 ┌─────────────┴─────────────┐
                 │                           │
                 ▼                           ▼
        ┌─────────────────┐        ┌─────────────────┐
        │    Chat LLM     │        │      RAG        │
        │      Groq       │        │                 │
        └─────────────────┘        └────────┬────────┘
                                             │
                                  ┌──────────▼──────────┐
                                  │ Hybrid Retrieval    │
                                  │                     │
                                  │ BM25 + Chroma/MMR  │
                                  └──────────┬──────────┘
                                             │
                                  ┌──────────▼──────────┐
                                  │     Documents       │
                                  │                     │
                                  │ PDF / TXT / Markdown│
                                  └─────────────────────┘