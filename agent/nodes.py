from llm.perplexity import call_perplexity

def retrieve_node(state):
    query = state["query"]
    retriever = state["retriever"]

    docs = retriever.invoke(query)

    # ✅ PASS query forward
    return {
        "query": query,
        "documents": docs
    }


def draft_answer_node(state):
    query = state["query"]
    docs = state["documents"]

    context = "\n\n".join(
        f"- {d.page_content}" for d in docs
    )

    prompt = f"""
You are a support knowledge-base assistant.
Answer ONLY using the context below.
If the answer is not present, say "I don't know".

Context:
{context}

Question:
{query}
"""

    answer = call_perplexity(prompt)

    return {
        "query": query,
        "draft_answer": answer,
        "sources": docs
    }


def final_answer_node(state):
    sources = state.get("sources", [])

    citations = list(
        set(d.metadata.get("source", "internal") for d in sources)
    )

    return {
        "final_answer": state["draft_answer"],
        "citations": citations
    }
