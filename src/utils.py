import json

import requests


def call_llm_stream(model, messages):
    url = 'http://localhost:11434/api/chat' # Using the chat endpoint
    data = {
        "model": model,
        "messages": messages, # Pass the list of messages
        "stream": True # Enable streaming
    }
    json_data = json.dumps(data)

    try:
        with requests.post(url, data=json_data, headers={"Content-Type": "application/json"}, stream=True) as response:
            response.raise_for_status() # Raises HTTPError for bad responses (4xx or 5xx)
            for chunk in response.iter_lines():
                if chunk:
                    try:
                        # Ollama sends one JSON object per line for streaming
                        json_chunk = json.loads(chunk.decode('utf-8'))
                        if "content" in json_chunk["message"]:
                            yield json_chunk["message"]["content"]
                        elif "done" in json_chunk and json_chunk["done"]:
                            break # End of stream
                    except json.JSONDecodeError:
                        # Handle malformed JSON if necessary
                        continue
    except requests.exceptions.ConnectionError:
        yield "Error: Could not connect to Ollama server. Is it running?"
    except requests.exceptions.RequestException as e:
        yield f"Error: An unexpected error occurred during the request: {e}"

# Non-streaming version:
def call_llm(model, prompt):
    url = 'http://localhost:11434/api/generate'
    data = {
        "model":model,
        "prompt":prompt,
        "stream":False
    }
    json_data = json.dumps(data)
    try:
        response = requests.post(url, data=json_data, headers={"Content-Type": "application/json"})
        response.raise_for_status() # Raises HTTPError for bad responses (4xx or 5xx)
        return response.json()
    except requests.exceptions.ConnectionError:
        return {"error": "Could not connect to Ollama server. Is it running?"}
    except requests.exceptions.RequestException as e:
        return {"error": f"An unexpected error occurred during the request: {e}"}
