from langchain_core.prompts import ChatPromptTemplate

from core.llm import LLMFactory


class TitleGenerator:

    def __init__(self):

        self.chain = (
            ChatPromptTemplate.from_messages([
                (
                    "system",
                    """
                You generate chat titles.

                Rules:
                - Maximum 3 words.
                - Noun phrase only.
                - Never answer the question.
                - Never summarize the assistant response.
                - Never start with a verb.
                - No punctuation.
                - No quotes.

                Examples:

                Question:
                "What is PCA?"
                Title:
                PCA

                Question:
                "How does Docker networking work?"
                Title:
                Docker Networking

                Question:
                "Explain attention mechanism"
                Title:
                Attention Mechanism

                Return ONLY the title.
                """
                ),
                                (
                    "human",
                    "{question}"
                )
            ])
            | LLMFactory.get_llm()
        )

    def generate(self, question):

        return self.chain.invoke(
            {
                "question": question
            }
        ).content.strip()