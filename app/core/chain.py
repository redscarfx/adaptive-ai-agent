from langchain_core.output_parsers import StrOutputParser

from core.llm import LLMFactory
from core.prompt_builder import build_prompt


class ChatChain:

    def __init__(self, profile):

        llm = LLMFactory.get_llm()

        prompt = build_prompt(profile)

        self.chain = prompt | llm | StrOutputParser()

        
    def stream(self, history, question):

        return self.chain.stream(
            {
                "history": history,
                "input": question,
            }
        )