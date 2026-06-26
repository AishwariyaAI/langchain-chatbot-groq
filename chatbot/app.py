import streamlit as st
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Load environment variables
load_dotenv()

# Get Groq API Key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

# ---------------- SIDEBAR ---------------- #
st.sidebar.title("⚙️ Chat Settings")

model = st.sidebar.selectbox(
    "Choose Model",
    [
        "llama-3.3-70b-versatile",
        "llama-3.1-8b-instant"
    ]
)

temperature = st.sidebar.slider(
    "Temperature",
    min_value=0.0,
    max_value=1.0,
    value=0.7,
    step=0.1
)

if st.sidebar.button("🗑 Clear Chat"):
    st.session_state.messages = []
    st.rerun()

# ---------------- LLM ---------------- #
llm = ChatGroq(
    api_key=GROQ_API_KEY,
    model=model,
    temperature=temperature
)

# ---------------- TITLE ---------------- #
st.title("🤖 AI Chatbot")
st.write("Built with **LangChain + Groq + Streamlit**")

# ---------------- CHAT HISTORY ---------------- #
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ---------------- USER INPUT ---------------- #
user_input = st.chat_input("Ask me anything...")

if user_input:

    # Show user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    try:
        # Get AI response
        response = llm.invoke(user_input)
        answer = response.content

        # Save AI response
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

        with st.chat_message("assistant"):
            st.markdown(answer)

    except Exception as e:
        st.error(f"❌ Error: {e}")