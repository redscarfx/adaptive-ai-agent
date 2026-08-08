from pathlib import Path
import os
from langchain_core.documents import Document

from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
    WebBaseLoader,
)

os.environ.setdefault(
    "USER_AGENT",
    os.getenv("USER_AGENT", "Adaptive-AI-Agent/1.0"),
)

class DocumentLoader:

    @staticmethod
    def load_pdf(path: str):

        return PyPDFLoader(path).load()

    @staticmethod
    def load_txt(path: str):

        return TextLoader(
            path,
            encoding="utf-8",
        ).load()

    @staticmethod
    def load_url(url: str):

        return WebBaseLoader(url).load()

    @staticmethod
    def load_markdown(path: str):

        text = Path(path).read_text(
            encoding="utf-8"
        )

        return [
            Document(
                page_content=text,
                metadata={
                    "source": path,
                },
            )
        ]