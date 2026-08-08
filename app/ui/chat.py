import streamlit as st

from langchain_core.messages import (
    HumanMessage,
    AIMessage,
)


def initialize_chat():

    if "messages" not in st.session_state:

        st.session_state.messages = []


def display_chat():

    for message in st.session_state.messages:

        role = (
            "user"
            if isinstance(message, HumanMessage)
            else "assistant"
        )

        with st.chat_message(role):
            st.markdown(message.content)


def add_user_message(content: str):

    st.session_state.messages.append(
        HumanMessage(content=content)
    )


def add_ai_message(content: str):

    st.session_state.messages.append(
        AIMessage(content=content)
    )
    
def clear_chat():
    st.session_state.messages = []