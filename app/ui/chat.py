import streamlit as st

from langchain_core.messages import (
    HumanMessage,
)

from core.conversation_manager import ConversationManager


def display_chat():

    for message in ConversationManager.current_messages():

        role = (
            "user"
            if isinstance(message, HumanMessage)
            else "assistant"
        )

        with st.chat_message(role):

            st.markdown(message.content)