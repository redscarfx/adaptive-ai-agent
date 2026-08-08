import os

os.environ["HF_HUB_OFFLINE"] = "1"
os.environ["TRANSFORMERS_OFFLINE"] = "1"

from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings


class VectorStore:

    def __init__(self):

        self.embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

        self.db = Chroma(
            persist_directory="data/chroma",
            embedding_function=self.embeddings,
        )

    def add_documents(self, documents):
        if self.db._collection.count() > 0:
            print("Vector database already exists.")
            return
        self.db.add_documents(documents)

        print(
            f"Indexed {self.db._collection.count()} chunks."
        )

    def similarity_search(
        self,
        query: str,
        k: int = 4,
    ):

        return self.db.similarity_search(
            query,
            k=k,
        )

    def as_retriever(
        self,
        search_type="similarity",
        search_kwargs=None,
    ):

        if search_kwargs is None:
            search_kwargs = {
                "k": 4,
            }

        return self.db.as_retriever(
            search_type=search_type,
            search_kwargs=search_kwargs,
        )
    
    def retriever(self):

        return self.db.as_retriever(
            search_type="similarity",
            search_kwargs={
                "k": 4,
            },
        )
    
    def add_file(
        self,
        chunks,
    ):

        self.db.add_documents(chunks)