import streamlit as st

from core.prompt_builder import UserProfile


def profile_sidebar() -> UserProfile:
    st.sidebar.title("👤 Profile")

    name = st.sidebar.text_input(
        "Name",
        value="Samuel",
    )

    age = st.sidebar.number_input(
        "Age",
        10,
        100,
        25,
    )

    city = st.sidebar.text_input(
        "City",
        value="Paris",
    )

    profession = st.sidebar.text_input(
        "Profession",
        value="Librarian",
    )

    interests = st.sidebar.text_area(
        "Interests",
        value="History of art",
    )

    language = st.sidebar.selectbox(
        "Language",
        [
            "English",
            "French",
        ],
    )

    answer_style = st.sidebar.selectbox(
        "Answer style",
        [
            "Technical",
            "Concise",
            "Educational",
            "Detailed",
            "Artistic",
        ],
    )

    return UserProfile(
        name=name,
        age=age,
        city=city,
        profession=profession,
        interests=interests,
        language=language,
        answer_style=answer_style,
    )