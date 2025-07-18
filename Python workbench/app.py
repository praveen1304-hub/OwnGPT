import streamlit as st
from datetime import datetime
from callollama import callOLLAMA

st.set_page_config(page_title="Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello, I am a smart chatbot. How can I help you?"}
    ]

if "is_typing" not in st.session_state:
    st.session_state.is_typing = False

st.title("GPT LLM")
st.markdown("Welcome to the session of GPT LLM")
st.subheader("Chat here")

for message in st.session_state.messages:
    if message["role"] == "user":
        st.info(f"You: {message['content']}")
    else:
        st.success(f"Bot: {message['content']}")

if st.session_state.is_typing:
    st.warning("Bot is typing...")

st.markdown("----")
st.subheader("Your Message")

with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("Type your message", placeholder="Ask me anything...")
    send_button = st.form_submit_button("Send Message", type="primary")

if send_button and user_input.strip():
    st.session_state.messages.append({"role": "user", "content": user_input.strip()})
    st.session_state.is_typing = True
    st.rerun()

if st.session_state.is_typing:
    user_message = st.session_state.messages[-1]["content"]
    bot_response = callOLLAMA(user_message)

    st.session_state.messages.append({"role": "assistant", "content": bot_response})
    st.session_state.is_typing = False
    st.rerun()

if st.button("Clear Chat"):
    st.session_state.messages = []
    st.rerun()
