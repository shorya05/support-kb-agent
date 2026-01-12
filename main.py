# from ingest.loader import load_documents
# from ingest.chunker import chunk_documents
# from rag.vectorstore import create_vectorstore
# from rag.retriever import get_retriever
# from agent.graph import build_graph

# def main():
#     docs = load_documents()
#     chunks = chunk_documents(docs)
#     vectorstore = create_vectorstore(chunks)
#     retriever = get_retriever(vectorstore)

#     graph = build_graph()

#     while True:
#         query = input("\nAsk a question (or type exit): ")
#         if query.lower() == "exit":
#             break

#         result = graph.invoke({
#             "query": query,
#             "retriever": retriever
#         })

#         print("\nAnswer:\n", result["final_answer"])
#         print("\nSources:", result["citations"])

# if __name__ == "__main__":
#     main()
from ingest.loader import load_documents
from ingest.chunker import chunk_documents
from rag.vectorstore import create_vectorstore
from rag.retriever import get_retriever
from agent.graph import build_graph

def main():
    docs = load_documents()
    chunks = chunk_documents(docs)
    vectorstore = create_vectorstore(chunks)
    retriever = get_retriever(vectorstore)

    graph = build_graph()

    while True:
        query = input("\nAsk a question (or type exit): ").strip()

        # ✅ SMART EXIT HANDLING
        if "exit" in query.lower():
            print("Goodbye 👋")
            break

        result = graph.invoke({
            "query": query,
            "retriever": retriever
        })

        print("\nAnswer:\n", result["final_answer"])
        print("\nSources:", result["citations"])

if __name__ == "__main__":
    main()
