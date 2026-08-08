from core.llm import LLMFactory

from rag.ingest import IngestionPipeline
from rag.vectorstore import VectorStore
from rag.hybrid import HybridRetriever
from rag.upload import UploadManager

from graph.graph import AdaptiveGraph


class RAGService:

    def __init__(self):

        self.ingestion = IngestionPipeline()

        self.vectorstore = VectorStore()

        self.documents = self.ingestion.build()

        if self.documents:

            self.vectorstore.add_documents(
                self.documents
            )

        self._build_retriever()

        self._build_graph()

    def _build_retriever(self):

        self.retriever = HybridRetriever(
            self.documents,
            self.vectorstore,
        )

    def _build_graph(self):

        self.graph = AdaptiveGraph(
            llm=LLMFactory.get_llm(),
            retriever=self.retriever,
        )

    def add_document(
        self,
        uploaded_file,
    ):

        path = UploadManager.save(
            uploaded_file,
        )

        chunks = self.ingestion.build_single(
            path,
        )

        if not chunks:
            return

        self.documents.extend(
            chunks
        )

        self.vectorstore.add_documents(
            chunks
        )

        self._build_retriever()

        self._build_graph()

    def invoke(
        self,
        history,
        question,
    ):

        return self.graph.invoke(
            question=question,
            history=history,
        )