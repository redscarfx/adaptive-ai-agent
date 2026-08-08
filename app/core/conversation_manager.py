import streamlit as st

from langchain_core.messages import (
    HumanMessage,
    AIMessage,
)


class ConversationManager:

    @staticmethod
    def initialize():

        if "conversations" not in st.session_state:

            st.session_state.conversations = {
                "Chat 1": []
            }

            st.session_state.current_chat = "Chat 1"

    @staticmethod
    def current_name():

        return st.session_state.current_chat

    @staticmethod
    def current_messages():

        return st.session_state.conversations[
            st.session_state.current_chat
        ]

    @staticmethod
    def add_user(content: str):

        ConversationManager.current_messages().append(
            HumanMessage(content=content)
        )

    @staticmethod
    def add_ai(content: str):

        ConversationManager.current_messages().append(
            AIMessage(content=content)
        )

    @staticmethod
    def create():

        index = len(st.session_state.conversations) + 1

        name = f"Chat {index}"

        st.session_state.conversations[name] = []

        st.session_state.current_chat = name

    @staticmethod
    def switch(name: str):

        st.session_state.current_chat = name
    
    @staticmethod
    def is_current(name: str):

        return (
            st.session_state.current_chat == name
        )