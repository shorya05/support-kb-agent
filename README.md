Support Knowledge Base Agent

A minimal, end-to-end Support KB Agent built using LangGraph, Retrieval-Augmented Generation (RAG), and MCP-style tools, exposed via FastAPI.

The agent answers user queries only from ingested documents (PDFs, markdown files, and web pages).
If the information is not present, it safely responds with “I don’t know” to prevent hallucinations.

Tech Stack

LangGraph – agent orchestration

RAG – vector search with embeddings

MCP-style tools – structured context injection

Perplexity Sonar-Pro – grounded LLM reasoning

FastAPI – API serving layer

ChromaDB – vector database

Architecture
FastAPI → LangGraph → Retrieve (RAG) → LLM → Answer + Sources

LangGraph explicitly controls the execution flow:
Retrieve → Draft Answer → Final Answer

Features

Ingests PDFs, markdown files, and web pages

Vector-based semantic retrieval

MCP-style retrieval and metadata tools

Hallucination-safe responses

REST API with Swagger UI

Setup & Run
pip install -r requirements.txt
uvicorn api.app:app --reload

Open Swagger UI:

http://127.0.0.1:8000/docs

Sample Request
POST /ask
{
  "question": "What is LangChain?"
}

Sample Response
{
  "answer": "LangChain is an open-source framework for building LLM-powered applications.",
  "sources": ["data/sample_docs/langchain.md"]
}

If the answer is not in the knowledge base:

{
  "answer": "I don't know"
}

Design Notes

LangGraph provides explicit, debuggable orchestration

MCP principles avoid prompt stuffing by using structured tools

RAG grounding ensures factual and safe responses

Author
Shorya Agarwal