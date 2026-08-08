from typing import TypedDict

from langchain_core.documents import Document
from langchain_core.messages import BaseMessage


class GraphState(TypedDict):
    question: str
    history: list[BaseMessage]
    documents: list[Document]
    answer: str