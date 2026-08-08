import streamlit as st

from core.conversation_manager import ConversationManager


def conversations_panel():

    st.subheader("💬 Conversations")

    if st.button(
        "➕ New Chat",
        use_container_width=True,
    ):

        ConversationManager.create()

        st.rerun()

    st.divider()

    for conversation in st.session_state.conversations:

        if st.button(
            conversation,
            key=conversation,
            use_container_width=True,
        ):

            ConversationManager.switch(
                conversation
            )

            st.rerun()