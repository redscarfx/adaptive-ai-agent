from langchain_community.retrievers import BM25Retriever
from langchain_classic.retrievers import EnsembleRetriever


class HybridRetriever:

    def __init__(
        self,
        documents,
        vectorstore,
    ):

        vector = vectorstore.as_retriever(
            search_type="mmr",
            search_kwargs={
                "k": 4,
                "fetch_k": 20,
                "lambda_mult": 0.7,
            },
        )

        retrievers = [vector]
        weights = [1.0]

        # BM25 requires at least one document.
        if documents:

            bm25 = BM25Retriever.from_documents(
                documents
            )

            bm25.k = 4

            retrievers = [
                bm25,
                vector,
            ]

            weights = [
                0.35,
                0.65,
            ]

        self.retriever = EnsembleRetriever(
            retrievers=retrievers,
            weights=weights,
        )

    def invoke(self, query):
        documents = self.retriever.invoke(query)

        unique = []
        seen = set()

        for doc in documents:

            key = (
                doc.metadata.get("source"),
                doc.metadata.get("page"),
                doc.page_content[:200],
            )

            if key in seen:
                continue

            seen.add(key)
            unique.append(doc)

        return unique