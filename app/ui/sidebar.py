import streamlit as st

from core.prompt_builder import UserProfile
from core.conversation_manager import ConversationManager


def profile_sidebar() -> UserProfile:

    st.sidebar.title("🤖 Adaptive AI Agent")

    st.sidebar.subheader("Conversations")

    if st.sidebar.button(
        "➕",
        help="Create a new conversation",
        use_container_width=True,
    ):
        ConversationManager.create()
        st.rerun()

    for conversation in st.session_state.conversations:

        selected = ConversationManager.is_current(
            conversation
        )

        if st.sidebar.button(
            conversation,
            key=conversation,
            use_container_width=True,
            type="primary" if selected else "secondary",
        ):
            ConversationManager.switch(conversation)
            st.rerun()


    with st.sidebar.expander(
        "👤 Profile",
        expanded=False,
    ):

        name = st.text_input(
            "Name",
            value="Samuel",
        )

        age = st.number_input(
            "Age",
            10,
            100,
            25,
        )

        city = st.text_input(
            "City",
            value="Paris",
        )

        profession = st.text_input(
            "Profession",
            value="Librarian",
        )

        interests = st.text_area(
            "Interests",
            value="History of art",
        )

        language = st.selectbox(
            "Language",
            [
                "French",
                "English",
            ],
        )

        answer_style = st.selectbox(
            "Answer style",
            [
                "Technical",
                "Concise",
                "Educational",
                "Detailed",
                "Artistic",
            ],
        )


    with st.sidebar.expander(
        "🧠 Agent Inspector",
        expanded=False,
    ):
        st.checkbox("Show prompt")
        st.checkbox("Show history")
        st.checkbox("Show latency")
        st.checkbox("Show tokens")

    return UserProfile(
        name=name,
        age=age,
        city=city,
        profession=profession,
        interests=interests,
        language=language,
        answer_style=answer_style,
    )