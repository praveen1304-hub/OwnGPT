
________________________________________
🤖 Local GPT Chatbot using Ollama + Streamlit
This is a personal chatbot project that runs a local LLM (Large Language Model) using Ollama and provides a simple web interface through Streamlit.
💬 Ask anything — the chatbot responds using the locally hosted qwen2.5:0.5b model or any other supported Ollama model.
________________________________________
✨ Features
•	🧠 Chatbot powered by a local LLM (via Ollama)
•	🔁 Maintains chat history within the session
•	✍️ Shows typing status while processing
•	🧹 "Clear Chat" button to reset the session
________________________________________
🗂 Project Structure
.
├── app.py            # Streamlit interface for the chatbot
├── callollama.py     # Logic to call the Ollama LLM API
________________________________________
🛠 Requirements
•	Python 3.8 or higher
•	Ollama installed and running locally
•	One or more Ollama-compatible models (e.g., qwen2.5:0.5b)
Install Python dependencies:
pip install streamlit requests
________________________________________
📦 Install and Run Ollama
ollama run qwen2.5:0.5b
This downloads and launches the qwen2.5:0.5b model on http://localhost:11434.
________________________________________
▶️ Running the Chatbot
streamlit run app.py
Then go to your browser and open http://localhost:8501.
________________________________________
📋 How It Works
•	app.py creates a Streamlit UI that displays messages and handles user input.
•	callollama.py sends prompts to the local Ollama API and retrieves generated responses from the selected LLM.
________________________________________
🧪 Example Usage
Type something like:
What's the capital of Japan?
Or:
Explain Python decorators with examples.
________________________________________
🧠 Model Customization
You can switch models by editing this line in callollama.py:
"model": "qwen2.5:0.5b"
Change to any other available model in Ollama like llama3, mistral, etc.
________________________________________
📄 License
This project is open-source under the MIT License.
________________________________________

