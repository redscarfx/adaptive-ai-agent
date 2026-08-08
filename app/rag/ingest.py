from pathlib import Path

from rag.loaders import DocumentLoader
from rag.splitter import DocumentSplitter


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DOCUMENTS_DIR = PROJECT_ROOT / "data" / "documents"


class IngestionPipeline:

    def __init__(self):

        self.splitter = DocumentSplitter()

    def load_documents(self):

        documents = []

        DOCUMENTS_DIR.mkdir(
            parents=True,
            exist_ok=True,
        )

        for file in DOCUMENTS_DIR.iterdir():

            if not file.is_file():
                continue

            suffix = file.suffix.lower()

            if suffix == ".pdf":

                documents.extend(
                    DocumentLoader.load_pdf(
                        str(file)
                    )
                )

            elif suffix == ".txt":

                documents.extend(
                    DocumentLoader.load_txt(
                        str(file)
                    )
                )

            elif suffix == ".md":

                documents.extend(
                    DocumentLoader.load_markdown(
                        str(file)
                    )
                )

        return documents

    def build(self):

        docs = self.load_documents()

        if not docs:
            return []

        return self.splitter.split(docs)

    def build_single(self, path):

        path = Path(path)

        suffix = path.suffix.lower()

        if suffix == ".pdf":

            docs = DocumentLoader.load_pdf(
                str(path)
            )

        elif suffix == ".txt":

            docs = DocumentLoader.load_txt(
                str(path)
            )

        elif suffix == ".md":

            docs = DocumentLoader.load_markdown(
                str(path)
            )

        else:

            raise ValueError(
                f"Unsupported file type: {suffix}"
            )

        return self.splitter.split(docs)