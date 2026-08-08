import streamlit as st


def initialize_conversations():

    if "conversations" not in st.session_state:

        st.session_state.conversations = {
            "💬 Chat 1": st.session_state.messages
        }

        st.session_state.current_chat = "💬 Chat 1"


def conversations_panel():

    initialize_conversations()

    st.subheader("💬 Conversations")

    if st.button(
        "➕ New Chat",
        use_container_width=True,
    ):
        pass

    st.divider()

    for conversation in st.session_state.conversations:

        st.button(
            conversation,
            key=conversation,
            use_container_width=True,
        )