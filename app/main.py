import streamlit as st

from ui.sidebar import profile_sidebar
from ui.chat import display_chat

from core.chain import ChatChain
from core.rag_service import RAGService
from core.conversation_manager import ConversationManager
from core.title_generator import TitleGenerator


st.set_page_config(
    page_title="Adaptive AI Agent",
    page_icon="🤖",
    layout="wide",
)


# --------------------------------------------------
# Initialization
# --------------------------------------------------

ConversationManager.initialize()

if "rag" not in st.session_state:
    st.session_state.rag = RAGService()

profile = profile_sidebar()

chat_chain = ChatChain(profile)

title_generator = TitleGenerator()


# --------------------------------------------------
# UI
# --------------------------------------------------

st.title("🤖 Adaptive AI Agent")

display_chat()


# --------------------------------------------------
# Input
# --------------------------------------------------

prompt = st.chat_input(
    "Ask anything..."
)


# --------------------------------------------------
# Processing
# --------------------------------------------------

if prompt:

    first_message = ConversationManager.is_empty()

    ConversationManager.add_user(prompt)

    # --------------------------------------------------
    # Generate conversation title
    # --------------------------------------------------

    if first_message:

        try:

            title = title_generator.generate(
                prompt
            )

            ConversationManager.rename(
                ConversationManager.current_name(),
                f"💬 {title}",
            )

        except Exception as e:

            st.warning(
                f"Title generation failed: {e}"
            )

    # --------------------------------------------------
    # Response
    # --------------------------------------------------

    placeholder = st.empty()

    with st.spinner("Thinking..."):

        # ==================================================
        # RAG
        # ==================================================

        if st.session_state.get(
            "use_rag",
            False,
        ):

            result = st.session_state.rag.invoke(
                ConversationManager.current_messages(),
                prompt,
            )

            response = result["answer"]

            placeholder.markdown(
                response
            )

            documents = result.get(
                "documents",
                [],
            )

            if documents:

                with st.expander(
                    "📄 Sources"
                ):

                    for doc in documents:

                        source = doc.metadata.get(
                            "source",
                            "Unknown",
                        )

                        page = doc.metadata.get(
                            "page",
                            "-",
                        )

                        st.markdown(
                            f"- **{source}** "
                            f"(page {page})"
                        )

        # ==================================================
        # Normal Chat
        # ==================================================

        else:

            response = ""

            for chunk in chat_chain.stream(
                ConversationManager.current_messages(),
                prompt,
            ):

                response += chunk

                placeholder.markdown(
                    response + "▌"
                )

            placeholder.markdown(
                response
            )

    ConversationManager.add_ai(
        response
    )

    st.rerun()