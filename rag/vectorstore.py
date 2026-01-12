from langchain_community.vectorstores import Chroma
from rag.embeddings import get_embeddings

def create_vectorstore(docs, persist_dir="chroma_db"):
    embeddings = get_embeddings()
    return Chroma.from_documents(
        docs,
        embedding=embeddings,
        persist_directory=persist_dir
    )
