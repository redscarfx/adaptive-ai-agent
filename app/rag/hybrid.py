from langchain_community.retrievers import BM25Retriever
from langchain_classic.retrievers import EnsembleRetriever


class HybridRetriever:

    def __init__(
        self,
        documents,
        vectorstore,
    ):

        bm25 = BM25Retriever.from_documents(documents)
        bm25.k = 4

        vector = vectorstore.as_retriever(
            search_type="mmr",
            search_kwargs={
                "k": 4,
                "fetch_k": 20,
                "lambda_mult": 0.7,
            },
        )

        self.retriever = EnsembleRetriever(
            retrievers=[
                bm25,
                vector,
            ],
            weights=[
                0.35,
                0.65,
            ],
        )

    def invoke(self, query):

        return self.retriever.invoke(query)