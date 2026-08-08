from pydantic import BaseModel

from langchain_core.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
)

from prompts.system_prompt import SYSTEM_PROMPT


class UserProfile(BaseModel):

    name: str

    age: int

    city: str

    profession: str

    interests: str

    language: str

    answer_style: str


def build_prompt(profile: UserProfile):

    system = f"""
{SYSTEM_PROMPT}

User Profile

Name: {profile.name}

Age: {profile.age}

City: {profile.city}

Profession: {profile.profession}

Interests:
{profile.interests}

Preferred language:
{profile.language}

Preferred style:
{profile.answer_style}
"""

    return ChatPromptTemplate.from_messages(
        [
            ("system", system),
            MessagesPlaceholder("history"),
            ("human", "{input}"),
        ]
    )