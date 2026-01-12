from fastapi import FastAPI
from pydantic import BaseModel

from ingest.loader import load_documents
from ingest.chunker import chunk_documents
from rag.vectorstore import create_vectorstore
from rag.retriever import get_retriever
from agent.graph import build_graph

# ---------- App ----------
app = FastAPI(title="Support KB Agent")

# ---------- Load once at startup ----------
docs = load_documents()
chunks = chunk_documents(docs)
vectorstore = create_vectorstore(chunks)
retriever = get_retriever(vectorstore)
graph = build_graph()

# ---------- Request schema ----------
class QueryRequest(BaseModel):
    question: str

# ---------- Health check ----------
@app.get("/health")
def health():
    return {"status": "ok"}

# ---------- Main RAG endpoint ----------
@app.post("/ask")
def ask_question(request: QueryRequest):
    result = graph.invoke({
        "query": request.question,
        "retriever": retriever
    })

    return {
        "question": request.question,
        "answer": result["final_answer"],
        "sources": result["citations"]
    }
