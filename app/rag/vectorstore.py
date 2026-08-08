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

        self.db.add_documents(documents)
        print(self.db._collection.count())

    def similarity_search(
        self,
        query: str,
        k: int = 4,
    ):

        return self.db.similarity_search(
            query,
            k=k,
        )

    def as_retriever(self):

        return self.db.as_retriever(
            search_kwargs={
                "k": 4,
            }
        )
    
    def retriever(self):

        return self.db.as_retriever(
            search_type="similarity",
            search_kwargs={
                "k": 4,
            },
        )