import streamlit as st

from ui.sidebar import profile_sidebar
from ui.chat import (
    initialize_chat,
    display_chat,
    add_message,
)

from core.prompt_builder import build_system_prompt

st.set_page_config(
    page_title="Adaptive AI Agent",
    page_icon="🤖",
    layout="wide",
)

initialize_chat()

profile = profile_sidebar()

system_prompt = build_system_prompt(profile)

st.title("🤖 Adaptive AI Agent")

st.caption(
    "Personalized AI Assistant powered by LangChain."
)

display_chat()

prompt = st.chat_input(
    "Ask anything..."
)

if prompt:

    add_message(
        "user",
        prompt,
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    response = (
        "🚀 LangChain agent will be connected "
        "in the next sprint."
    )

    add_message(
        "assistant",
        response,
    )

    with st.chat_message("assistant"):
        st.markdown(response)