from langchain_community.document_loaders import TextLoader
from pathlib import Path

def load_documents(data_path="data/sample_docs"):
    docs = []
    for file in Path(data_path).glob("*.md"):
        loader = TextLoader(str(file))
        docs.extend(loader.load())
    return docs
