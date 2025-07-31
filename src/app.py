import streamlit as st

from utils import call_llm_stream

# Configuration
AVAILABLE_MODELS = [
    "llama3.2",
    "llama3.2:1b",
    "gemma3",
    "gemma3:1b",
]

st.title("💬 LLM Chatbot")
st.caption(f"A Streamlit chatbot powered by Ollama :llama:")

# Sidebar for Model Selection
with st.sidebar:
    st.header("Model Configuration")
    selected_model = st.selectbox(
        "Choose an Ollama Model",
        AVAILABLE_MODELS,
        index=AVAILABLE_MODELS.index("llama3.2:1b") if "llama3.2:1b" in AVAILABLE_MODELS else 0, # Set default
        help="Select the model you want to use. Ensure it's running with 'ollama run <model_name>' on your machine."
    )
    st.info(f"**Selected Model:** `{selected_model}`\n\n"
            f"**IMPORTANT:** Please ensure this model is running in your terminal:\n"
            f"\n `ollama run {selected_model}`")

# Initialize Chat Messages
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

# Display Chat Messages
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Handle User Input
if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""

        # Prepare messages for the Ollama chat API
        # For simplicity, we'll send all current messages as roles.
        ollama_messages = [{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]

        try:
            # Pass the selected_model from the sidebar to call_llm_stream
            for chunk in call_llm_stream(selected_model, ollama_messages):
                full_response += chunk
                message_placeholder.markdown(full_response + "▌") # Add a blinking cursor
            message_placeholder.markdown(full_response) # Remove cursor at the end
            st.session_state.messages.append({"role": "assistant", "content": full_response})
        except Exception as e:
            # Enhanced error message for the user, specifically about Ollama connection
            if "Could not connect to Ollama server" in str(e):
                st.error("🚨 Error: Could not connect to the Ollama server. "
                         "Please ensure Ollama is running and the selected model is loaded "
                         f"in your terminal (e.g., `ollama run {selected_model}`).")
            else:
                st.error(f"An unexpected error occurred: {e}")
            st.session_state.messages.append({"role": "assistant", "content": f"Sorry, an error occurred: {e}"})
