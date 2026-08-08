import os
from langchain_groq import ChatGroq
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parents[2] / ".env")


class LLMFactory:
    @staticmethod
    def get_llm():

        return ChatGroq(
            api_key=os.getenv("GROQ_API_KEY"),
            model=os.getenv("MODEL_NAME", "llama-3.1-8b-instant"),
            temperature=0.3,
        )