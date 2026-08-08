import streamlit as st

from core.prompt_builder import UserProfile
from core.conversation_manager import ConversationManager


def profile_sidebar() -> UserProfile:

    # --------------------------------------------------
    # Header
    # --------------------------------------------------

    st.sidebar.title("🤖 Adaptive AI Agent")

    # --------------------------------------------------
    # Conversations
    # --------------------------------------------------

    st.sidebar.subheader("💬 Conversations")

    if st.sidebar.button(
        "➕",
        help="New conversation",
        use_container_width=True,
    ):
        ConversationManager.create()
        st.rerun()

    for conversation in st.session_state.conversations:

        selected = ConversationManager.is_current(conversation)

        if st.sidebar.button(
            conversation,
            key=conversation,
            use_container_width=True,
            type="primary" if selected else "secondary",
        ):
            ConversationManager.switch(conversation)
            st.rerun()

    st.sidebar.divider()

    # --------------------------------------------------
    # Knowledge
    # --------------------------------------------------

    st.sidebar.subheader("📚 Knowledge")

    uploaded = st.sidebar.file_uploader(
        "Upload document",
        type=["pdf", "txt", "md"],
    )

    if uploaded:

        key = f"indexed_{uploaded.name}"

        if key not in st.session_state:

            with st.spinner("Indexing document..."):

                st.session_state.rag.add_document(
                    uploaded
                )

            st.session_state[key] = True

            st.sidebar.success("Document indexed.")

    url = st.sidebar.text_input(
        "Website URL",
    )

    st.session_state.use_rag = st.sidebar.toggle(
        "Enable RAG",
        value=False,
    )

    st.sidebar.divider()

    # --------------------------------------------------
    # Profile
    # --------------------------------------------------

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

    # --------------------------------------------------
    # Inspector
    # --------------------------------------------------

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