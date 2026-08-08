from langchain_core.prompts import ChatPromptTemplate

from core.llm import LLMFactory


class TitleGenerator:

    def __init__(self):

        self.chain = (
            ChatPromptTemplate.from_messages([
                (
                    "system",
                    "Generate a conversation title in at most 4 words."
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