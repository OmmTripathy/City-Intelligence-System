import streamlit as st
from agent import chat_with_agent   # Change "main" if your file has another name

st.set_page_config(
    page_title="City Intelligence Agent",
    page_icon="🌍",
    layout="centered"
)

st.title("🌍 City Intelligence Agent")
st.caption("Ask about weather, news, or any city-related information.")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
prompt = st.chat_input("Ask something...")

if prompt:

    # Show user message
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    # Get AI response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = chat_with_agent(prompt)

        st.markdown(response)

    # Save assistant response
    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )