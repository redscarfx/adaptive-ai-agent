from langchain_core.prompts import ChatPromptTemplate

from core.llm import LLMFactory


class TitleGenerator:

    def __init__(self):

        self.chain = (
            ChatPromptTemplate.from_messages([
                (
                    "system",
                    """
                You are an expert conversation title generator.

                Your task is to generate a short title for a chat conversation.

                Rules:
                - The title must describe the MAIN topic of the user's FIRST message.
                - Ignore greetings, politeness and filler words.
                - Never answer the question.
                - Never summarize the assistant response.
                - Never generate a sentence.
                - Return ONLY the title.
                - Maximum 3 words.
                - Prefer noun phrases.
                - No punctuation.
                - No quotation marks.
                - No emojis.
                - No articles unless necessary (a, an, the).
                - If an acronym is the main topic, keep the acronym.
                - If a famous concept exists (e.g. PCA, Docker Networking, Ancient Egypt), use its common name.
                - The title should look like a ChatGPT conversation title.

                Examples

                User:
                Can you explain Principal Component Analysis with an intuitive example?

                Title:
                PCA

                ---

                User:
                I'm planning a three-week trip through Japan and I'm looking for an itinerary combining Tokyo, Kyoto, hiking and traditional villages.

                Title:
                Japan Travel

                ---

                User:
                I've been feeling mentally exhausted for several months despite sleeping well and exercising regularly. Could stress or burnout explain it?

                Title:
                Mental Fatigue

                ---

                User:
                I recently started cooking at home and I'd like to learn the basics, including essential techniques, recipes and kitchen equipment.

                Title:
                Learning Cooking

                ---

                User:
                I'm 24 years old and I'd like to start investing my savings. Could you explain ETFs, diversification and compound interest?

                Title:
                Personal Investing

                ---

                User:
                What's the difference between Stoicism and Existentialism?

                Title:
                Philosophy

                ---

                User:
                How can I debug Docker networking issues between multiple containers?

                Title:
                Docker Networking

                ---

                User:
                I'm building an AI assistant using LangChain, LangGraph and RAG.

                Title:
                LangChain Agent

                ---

                User:
                {question}

                Title:
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