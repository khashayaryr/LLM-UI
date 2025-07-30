import streamlit as st
from utils import call_llm


st.title("💬 LLM Chatbot")
st.caption("A Streamlit chatbot powered by Llama :llama:")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():

    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    with st.spinner("Generating response..."):
        msg = call_llm("llama3.2", prompt)["response"]
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)
