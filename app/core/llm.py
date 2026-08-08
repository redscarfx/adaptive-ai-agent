import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()


class LLMFactory:
    @staticmethod
    def get_llm():

        return ChatGroq(
            api_key=os.getenv("GROQ_API_KEY"),
            model=os.getenv("MODEL_NAME", "llama-3.1-8b-instant"),
            temperature=0.3,
        )