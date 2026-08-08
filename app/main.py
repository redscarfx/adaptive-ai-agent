import streamlit as st


from ui.sidebar import profile_sidebar
from ui.chat import (
    initialize_chat,
    display_chat,
    add_user_message,
    add_ai_message,
)
from ui.conversations import conversations_panel

from core.chain import ChatChain


st.set_page_config(
    page_title="Adaptive AI Agent",
    page_icon="🤖",
    layout="wide",
)


initialize_chat()



profile = profile_sidebar()



chat_chain = ChatChain(profile)








st.title("🤖 Adaptive AI Agent")

st.caption(
    "Personalized AI Assistant powered by LangChain."
)

left, right = st.columns(
    [2, 6],
    gap="medium",
)

with left:
    conversations_panel()

with right:
    display_chat()

prompt = st.chat_input(
    "Ask anything..."
)

if prompt:
    add_user_message(prompt)

    with st.chat_message("user"):
        st.markdown(prompt)


    response = ""

    with st.chat_message("assistant"):

        placeholder = st.empty()

        for chunk in chat_chain.stream(
            st.session_state.messages,
            prompt,
        ):
            response += chunk
            placeholder.markdown(response + "▌")

        placeholder.markdown(response)


    add_ai_message(response)
    st.rerun()
