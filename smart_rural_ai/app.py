import streamlit as st
from coordinator import CoordinatorAgent

st.set_page_config(page_title="Smart Rural AI", layout="centered")

bot = CoordinatorAgent()

st.title("🤖 Smart Rural AI Assistant")

if "chat" not in st.session_state:
    st.session_state.chat = []

for role, msg in st.session_state.chat:
    if role == "user":
        st.markdown(f"**You:** {msg}")
    else:
        st.markdown(f"**AI:** {msg}")

user_input = st.text_input("Ask something:")

if st.button("Send") and user_input:

    response = bot.handle(user_input)

    st.session_state.chat.append(("user", user_input))
    st.session_state.chat.append(("ai", response))

    st.rerun()