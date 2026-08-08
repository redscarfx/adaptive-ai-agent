from langgraph.graph import (
    StateGraph,
    START,
    END,
)

from graph.state import GraphState
from graph.nodes import retrieve, generate


class AdaptiveGraph:

    def __init__(self, llm, retriever):

        self.llm = llm
        self.retriever = retriever

        builder = StateGraph(GraphState)

        builder.add_node("retrieve", self.retrieve_node)
        builder.add_node("generate", self.generate_node)

        builder.add_edge(START, "retrieve")
        builder.add_edge("retrieve", "generate")
        builder.add_edge("generate", END)

        self.graph = builder.compile()

    def retrieve_node(self, state: GraphState):

        return retrieve(
            state,
            self.retriever,
        )

    def generate_node(self, state: GraphState):

        return generate(
            state,
            self.llm,
        )

    def invoke(self, question, history):

        return self.graph.invoke(
            {
                "question": question,
                "history": history,
            }
        )