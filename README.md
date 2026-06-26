# 🤖 LangChain Chatbot with Groq

A simple AI chatbot built using LangChain, Groq API, and Streamlit.

## 🚀 Deployment (Render)

## 🚀 Live Demo

🚧 **Coming Soon**

The application is currently under active development and testing. A public deployment will be available after completing additional LangChain features and stability improvements.

---

### Python Version

This project is developed and tested with **Python 3.11**.

You can specify the Python version by creating a `runtime.txt` file:

```text
python-3.11.9
```

Or set the Python version in Render if required.

---

### Environment Variables

Before running the application, configure the following environment variable in the Render Dashboard:

| Variable | Description |
|----------|-------------|
| `GROQ_API_KEY` | Your Groq API key for accessing the Llama model. |

Example:

```text
GROQ_API_KEY=your_groq_api_key
```

---

### Start Command

```bash
streamlit run chatbot/app.py --server.port $PORT --server.address 0.0.0.0
```

## 🚀 Features

- Chat with Llama 3 models using Groq
- Streamlit web interface
- Chat history
- Temperature control
- Model selection
- Secure API key using .env

## 🛠 Tech Stack

- Python
- LangChain
- Groq API
- Streamlit
- python-dotenv

## Installation

Clone the repository

```bash
git clone <your-repository-url>
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
GROQ_API_KEY=your_api_key_here
```

Run the project

```bash
streamlit run app.py
```

## Project Screenshot

![alt text](<My Chatbot.png>)

## Future Improvements

- Prompt Templates
- Chat Memory
- RAG Integration
- PDF Chatbot
- AI Agents
