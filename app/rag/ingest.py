from pathlib import Path

from rag.loaders import DocumentLoader
from rag.splitter import DocumentSplitter


class IngestionPipeline:

    def __init__(self):

        self.splitter = DocumentSplitter()

    def load_documents(self):

        documents = []

        folder = Path("data/documents")

        for file in folder.iterdir():

            suffix = file.suffix.lower()

            if suffix == ".pdf":

                documents.extend(
                    DocumentLoader.load_pdf(str(file))
                )

            elif suffix == ".txt":

                documents.extend(
                    DocumentLoader.load_txt(str(file))
                )

            elif suffix == ".md":

                documents.extend(
                    DocumentLoader.load_markdown(str(file))
                )

        return documents

    def build(self):

        docs = self.load_documents()

        chunks = self.splitter.split(
            docs
        )

        return chunks