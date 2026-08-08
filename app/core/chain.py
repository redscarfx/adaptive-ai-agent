""" from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables.history import RunnableWithMessageHistory

from core.llm import LLMFactory
from core.memory import ChatMemory
from core.prompt_builder import build_prompt


class ChatChain:

    def __init__(self, profile):

        llm = LLMFactory.get_llm()

        prompt = build_prompt(profile)

        chain = prompt | llm | StrOutputParser()

        self.memory = ChatMemory()

        self.chain = RunnableWithMessageHistory(
            chain,
            self.memory.get_history,
            input_messages_key="input",
            history_messages_key="history",
        )

    def invoke(self, session_id: str, question: str):

        return self.chain.invoke(
            {
                "input": question,
            },
            config={
                "configurable": {
                    "session_id": session_id,
                }
            },
        ) """
        

from langchain_core.output_parsers import StrOutputParser

from core.llm import LLMFactory
from core.prompt_builder import build_prompt


class ChatChain:

    def __init__(self, profile):

        llm = LLMFactory.get_llm()

        prompt = build_prompt(profile)

        self.chain = prompt | llm | StrOutputParser()

    def invoke(self, session_id: str, question: str):

        return self.chain.invoke(
            {
                "history": [],
                "input": question,
            }
        )
        
    def stream(self, history, question):

        return self.chain.stream(
            {
                "history": history,
                "input": question,
            }
        )