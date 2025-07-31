import streamlit as st

from utils import call_llm_stream

st.title("💬 LLM Chatbot")
st.caption("A Streamlit chatbot powered by Llama :llama:")

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        # Pass the entire conversation history to the LLM
        # Prepare messages for the Ollama chat API
        ollama_messages = [{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]

        try:
            for chunk in call_llm_stream("llama3.2:1b", ollama_messages):
                full_response += chunk
                message_placeholder.markdown(full_response + "▌") # Add a blinking cursor
            message_placeholder.markdown(full_response) # Remove cursor at the end
            st.session_state.messages.append({"role": "assistant", "content": full_response})
        except Exception as e:
            st.error(f"An error occurred: {e}")
            st.session_state.messages.append({"role": "assistant", "content": f"Sorry, an error occurred: {e}"})
