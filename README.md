## Title : AI Smart Chatbot

A web-based AI chatbot built using Flask, Groq's LLaMA 3.3 70B model, HTML, CSS, and JavaScript. The application maintains conversational context through chat history and provides real-time responses via a browser-based interface.

## Abstract

This project is a web-based AI chatbot built using Flask and Groq's LLaMA 3.3 70B language model. The application provides a simple browser-based chat interface that allows users to interact with a large language model in real time.

The system follows a client-server architecture where the frontend, developed using HTML, CSS, and JavaScript, communicates with a Flask backend through asynchronous HTTP requests. When a user submits a message, the frontend sends the input to the backend via a POST request. Flask receives the message, maintains the conversation history, and forwards the complete chat context to Groq's API. The LLaMA model generates a context-aware response, which is returned to the frontend in JSON format and displayed within the chat interface.

The chatbot preserves conversational continuity by storing both user and assistant messages, enabling multi-turn interactions. API credentials are managed securely using environment variables loaded through the python-dotenv package.

This project demonstrates the integration of modern Large Language Models (LLMs) into web applications while showcasing concepts such as RESTful communication, API integration, context management, JSON data exchange, and full-stack AI application development.

## Key Concepts Demonstrated

- Flask Web Development
- REST API Endpoints
- Frontend-Backend Communication
- JSON Data Exchange
- Environment Variable Management
- LLM API Integration
- Conversational Context Preservation
- Prompt and Chat History Management
- Client-Server Architecture

## System Workflow

```text
┌──────────────┐
│ User Message │
└──────┬───────┘
       ↓
┌─────────────────────────┐
│ JavaScript Fetch Request│
└──────┬──────────────────┘
       ↓
┌──────────────────────┐
│ Flask Backend (/chat)│
└──────┬───────────────┘
       ↓
┌──────────────────────┐
│ Chat History Manager │
└──────┬───────────────┘
       ↓
┌──────────────────────┐
│ Groq API (LLaMA 3.3) │
└──────┬───────────────┘
       ↓
┌──────────────────────┐
│   Model Response     │
└──────┬───────────────┘
       ↓
┌──────────────────────┐
│    JSON Response     │
└──────┬───────────────┘
       ↓
┌──────────────────────┐
│ Chat Interface Update│
└──────────────────────┘
```

## Project Structure

```text
chatbot/
│
├── app.py
│
├── static/
│   ├── style.css
│   └── script.js
│
├── templates/
│   └── index.html
│
├── .env
├── .gitignore
└── README.md
```

### File Description

- **app.py** – Flask backend application responsible for routing, chat history management, API communication, and response handling.
- **templates/index.html** – Frontend user interface for the chatbot.
- **static/style.css** – Styling for the chat interface.
- **static/script.js** – Handles frontend logic, user interactions, and communication with the Flask backend.
- **.env** – Stores sensitive environment variables such as the Groq API key.
- **README.md** – Project documentation.

---

## Technologies Used

### Backend
- Python
- Flask
- Groq API
- Python Dotenv

### Frontend
- HTML
- CSS
- JavaScript

### AI Model
- LLaMA 3.3 70B Versatile

---

## Features

- Real-time chatbot interface
- Integration with Groq's LLaMA 3.3 70B model
- Context-aware conversations through chat history
- JSON-based frontend-backend communication
- RESTful API endpoint implementation
- Secure API key management using environment variables
- Lightweight and modular architecture

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/Blackblitz777/flask-chatbot.git
cd chatbot
```

### Create a Virtual Environment

```bash
python -m venv venv
```

### Activate the Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Linux / WSL:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install flask groq python-dotenv
```

### Configure Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY="my_api_key_here"
```

### Run the Application

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

in your browser.

---

## Usage

1. Open the chatbot in a web browser.
2. Type a message into the chat input field.
3. The frontend sends the message to the Flask backend.
4. The backend forwards the conversation history to Groq's LLaMA model.
5. The model generates a response.
6. The response is returned to the frontend and displayed in the chat window.
7. The conversation history is maintained to preserve context across interactions.

---

## Learning Outcomes

This project helped demonstrate:

- Client-Server Architecture
- Flask Routing
- REST API Design
- JSON Data Exchange
- Environment Variable Management
- LLM API Integration
- Conversational Memory Handling
- Frontend-Backend Communication
- AI Application Development

---

## Future Improvements

- Persistent chat history using a database
- User authentication and session management
- Multiple model selection
- Streaming responses
- Conversation export functionality
- Responsive mobile interface
- Deployment using Docker and cloud platforms
- Retrieval-Augmented Generation (RAG)
- Agentic workflows and tool calling

---

## Author

Developed as part of Generative AI and Large Language Model learning and experimentation.

