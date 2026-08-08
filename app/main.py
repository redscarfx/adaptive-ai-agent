import streamlit as st

from langchain_core.messages import (
    HumanMessage,
    AIMessage,
)

from ui.sidebar import profile_sidebar
from ui.chat import (
    initialize_chat,
    display_chat,
    add_message,
)

from core.chain import ChatChain


st.set_page_config(
    page_title="Adaptive AI Agent",
    page_icon="🤖",
    layout="wide",
)

# ---------- Session ----------

initialize_chat()

if "history" not in st.session_state:
    st.session_state.history = []

# ---------- User Profile ----------

profile = profile_sidebar()

# Toujours reconstruire la chaîne
# afin que les modifications du profil
# soient immédiatement prises en compte.

chat_chain = ChatChain(profile)

# ---------- UI ----------

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


    response = ""

    with st.chat_message("assistant"):

        placeholder = st.empty()

        for chunk in chat_chain.stream(
            st.session_state.history,
            prompt,
        ):
            response += chunk
            placeholder.markdown(response + "▌")

        placeholder.markdown(response)


    st.session_state.history.append(
        HumanMessage(content=prompt)
    )

    st.session_state.history.append(
        AIMessage(content=response)
    )

    add_message(
        "assistant",
        response,
    )

