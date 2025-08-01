# 💬 Streamlit Ollama Chatbot

A simple yet powerful chatbot built with **Streamlit** for the user interface and powered by **Ollama** for local large language model (LLM) inference. This project allows you to interact with various Ollama-compatible models (like Llama 3.2) directly from your browser, with the flexibility to switch models via the Streamlit UI.


## ✨ Features

* **Interactive Chat Interface:** A clean and intuitive chat UI powered by Streamlit.
* **Local LLM Inference:** Utilizes Ollama to run large language models directly on your machine, ensuring data privacy and offline capability.
* **Conversation History:** Maintains context across turns, allowing for more coherent and natural conversations.
* **Streaming Responses:** Get real-time feedback as the LLM generates its reply, token by token.
* **Dynamic Model Selection:** Choose your desired Ollama model from a sidebar within the Streamlit application.


## 🛠️ Prerequisites

Before you begin, ensure you have the following installed:

1.  **Ollama:** The Ollama server and CLI tool.

    * Run the install script for Linux or WSL terminal:
    ```bash
    curl -fsSL https://ollama.com/install.sh | sh
    ```
    * Alternatively, you can download and install it from the [Ollama website](https://ollama.com/download) for the Windows or macOS.   


2.  **Models for Ollama:** Pull the LLM models you wish to use with Ollama. For example, to use Llama 3.2 (recommended for this project):
    ```bash
    ollama pull llama3.2
    ```
    Or if you prefer a smaller version:
    ```bash
    ollama pull llama3.2:1b
    ```
    Another example model:
    ```bash
    ollama pull gemma3
    ```
    You can explore more models on the [Ollama Models page](https://ollama.com/library).
    > **Note:**   
    > You should have at least 8 GB of RAM available to run the 7B models, 16 GB to run the 13B models, and 32 GB to run the 33B models.

3.  **Python 3.8+**



## 🚀 Installation

Follow these steps to get your chatbot up and running:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/khashayaryr/LLM-UI.git
    ```

2.  **Navigate to the project's root directory in your terminal:**
    ```bash
    cd LLM-UI
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## 🏃 How to Run

You need to run the Ollama model in a separate terminal window so that your Streamlit application can connect to it and then, run the streamlit application.   
Follow these steps:

1.  **Choose the model you want to use from your pulled models (e.g., llama3.2) and run:**
    ```bash
    ollama run llama3.2
    ```
    > Keep this terminal window open and running. If you want to switch models in the Streamlit UI later, you'll need to stop the currently running model (Ctrl+C or Ctrl+D in the terminal) and start the new one.

2.  **In a new terminal window (with your virtual environment activated), navigate to your `LLM-UI` directory and add the current directory to your `PYTHONPATH` to ensure Python can find the `src` module:**
    ```bash
    cd LLM-UI
    export PYTHONPATH=$PYTHONPATH:$(pwd)
    ```

3.  **Run the Streamlit application::**
    ```bash
    streamlit run src/app.py
    ```
    Your browser should automatically open a new tab with the Streamlit chatbot application. If not, open your browser and navigate to [http://localhost:8501](http://localhost:8501).

## 💡 Usage

1.  **Select a Model:** On the left sidebar, use the dropdown menu under "Model Configuration" to choose the Ollama model you want to interact with.
2.  **Ensure Model is Running:** Remember the important instruction in the sidebar to run `ollama run <selected_model>` in your terminal.
3.  **Start Chatting:** Type your message in the input box at the bottom and press Enter. The LLM's response will stream back to you.


## 📁 Project Structure
```
.
├── .gitignore                      # Specifies intentionally untracked files to ignore
├── LICENSE                         # MIT License
├── README.md                       # This file
├── requirements.txt                # Project dependencies
└── src/
    ├── app.py                      # Main Streamlit UI application
    └── utils.py                    # Utility functions for Ollama API interaction
```

## 🤝 Contributing

Feel free to fork this repository and contribute! If you have suggestions for improvements or find any issues, please open an issue or submit a pull request.

## 📄 License

This project is open source and available under the [MIT License](https://github.com/khashayaryr/LLM-UI/blob/main/LICENSE).