from graph.state import GraphState

from langchain_core.documents import Document
from langchain_core.messages import HumanMessage, SystemMessage


def retrieve(state: GraphState, retriever):

    docs = retriever.invoke(state["question"])

    return {
        "documents": docs,
    }


def generate(state: GraphState, llm):

    docs = state["documents"]

    context = "\n\n".join(
        f"[Document {i+1}]\n{doc.page_content}"
        for i, doc in enumerate(docs)
    )

    messages = [
        SystemMessage(
            content="""
You are a Retrieval-Augmented AI assistant.

Answer ONLY using the provided context.

If the answer is not present in the context,
reply exactly:

I don't know.

Always be precise.
"""
        ),
        HumanMessage(
            content=f"""
Context:

{context}

Question:

{state["question"]}
"""
        ),
    ]

    response = llm.invoke(messages)

    return {
        "answer": response.content,
    }