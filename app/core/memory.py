from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory


class ChatMemory:

    def __init__(self):

        self.store = {}

    def get_history(self, session_id: str):

        if session_id not in self.store:

            self.store[session_id] = InMemoryChatMessageHistory()

        return self.store[session_id]