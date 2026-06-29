# ============================================================
#                 IMPORT LIBRARIES
# ============================================================

import uuid
import streamlit as st

from agent import chat_with_agent


# ============================================================
#                 PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="City Intelligence Agent",
    page_icon="🌍",
    layout="wide"
)


# ============================================================
#                 PAGE TITLE
# ============================================================

st.title("🌍 City Intelligence Agent")
st.caption("Ask anything about a city.")


# ============================================================
#                 SESSION STATE
# ============================================================

# Store conversation history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Store thread ID for LangGraph memory
if "thread_id" not in st.session_state:
    st.session_state.thread_id = str(uuid.uuid4())


# ============================================================
#                 SIDEBAR
# ============================================================

with st.sidebar:

    st.header("About")

    st.write("""
This AI Agent can:

- 🌤️ Check Weather
- 📰 Fetch Latest News
- 🤖 Answer General Questions

Built using:
- Streamlit
- LangChain
- Mistral AI
- Tavily
- OpenWeather API
""")

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.session_state.thread_id = str(uuid.uuid4())
        st.rerun()


# ============================================================
#                 DISPLAY OLD MESSAGES
# ============================================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# ============================================================
#                 CHAT INPUT
# ============================================================

user_prompt = st.chat_input("Ask me something...")


# ============================================================
#                 PROCESS USER MESSAGE
# ============================================================

if user_prompt:

    # Show user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(user_prompt)

    # Generate AI response
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            response = chat_with_agent(
                user_prompt,
                thread_id=st.session_state.thread_id
            )

        st.markdown(response)

    # Save AI response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )