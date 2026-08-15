import streamlit as st

from chatbot import FAQChatbot


st.set_page_config(
    page_title="IIM Lucknow FAQ Chatbot",
    page_icon="🏫"
)


@st.cache_resource
def load_chatbot():

    return FAQChatbot("faq_data.json")


chatbot = load_chatbot()


st.title("🏫 IIM Lucknow FAQ Chatbot")

st.write(
    "Ask your questions about IIM Lucknow."
)


if "messages" not in st.session_state:

    st.session_state.messages = []


for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.write(message["content"])


user_question = st.chat_input(
    "Ask a question..."
)


if user_question:

    st.session_state.messages.append({
        "role": "user",
        "content": user_question
    })

    with st.chat_message("user"):

        st.write(user_question)


    answer, score = chatbot.get_response(
        user_question
    )


    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })

    with st.chat_message("assistant"):

        st.write(answer)

        st.caption(
            f"Similarity score: {score:.2%}"
        )


if st.button("🗑️ Clear Chat"):

    st.session_state.messages = []

    st.rerun()