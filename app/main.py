import streamlit as st

from ui.sidebar import profile_sidebar
from ui.chat import display_chat

from core.conversation_manager import ConversationManager
from core.chain import ChatChain
from core.title_generator import TitleGenerator

st.set_page_config(
    page_title="Adaptive AI Agent",
    page_icon="🤖",
    layout="wide",
)

st.markdown("""
<style>

/* Header Streamlit */
[data-testid="stHeader"]{
    display:none;
}

/* Supprime la marge haute du contenu */
.block-container{
    padding-top:1rem;
}

/* Supprime la marge haute de la sidebar */
[data-testid="stSidebarContent"]{
    padding-top:0rem;
}

/* Colle le premier élément en haut */
[data-testid="stSidebarContent"] > div:first-child{
    margin-top:-3.2rem;
}

/* Réduit les espaces entre éléments */
[data-testid="stVerticalBlock"]{
    gap:0.5rem;
}

</style>
""", unsafe_allow_html=True)

ConversationManager.initialize()

profile = profile_sidebar()

chat_chain = ChatChain(profile)
title_generator = TitleGenerator()

st.title("🤖 Adaptive AI Agent")

st.sidebar.markdown(
    "<small>Powered by LangChain</small>",
    unsafe_allow_html=True,
)

display_chat()

prompt = st.chat_input("Ask anything...")

if prompt:

    ConversationManager.add_user(prompt)
    
    if ConversationManager.is_empty():

        old_name = ConversationManager.current_name()

        try:

            title = title_generator.generate(prompt)

            
            ConversationManager.rename(
                old_name,
                f"💬 {title}"
            )

        except Exception:

            pass

    with st.spinner("Thinking..."):

        response = ""

        placeholder = st.empty()

        for chunk in chat_chain.stream(
            ConversationManager.current_messages(),
            prompt,
        ):
            response += chunk
            placeholder.markdown(response + "▌")

        placeholder.markdown(response)

    ConversationManager.add_ai(response)

    st.rerun()