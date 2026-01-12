def search_kb(retriever, query: str):
    docs = retriever.invoke(query)

    return [
        {
            "content": d.page_content,
            "source": d.metadata.get("source", "unknown")
        }
        for d in docs
    ]
