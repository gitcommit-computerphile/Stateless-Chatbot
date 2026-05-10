import streamlit as st
from chain import get_response

st.set_page_config(page_title="Stateless Chatbot", layout="centered")
st.title("Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_input = st.chat_input("Ask me anything...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = get_response(user_input)
        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
