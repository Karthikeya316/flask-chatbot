##Title : AI Smart Chatbot

A web-based AI chatbot built using Flask, Groq's LLaMA 3.3 70B model, HTML, CSS, and JavaScript. The application maintains conversational context through chat history and provides real-time responses via a browser-based interface.
## Abstract

This project is a web-based AI chatbot built using Flask and Groq's LLaMA 3.3 70B language model. The application provides a simple browser-based chat interface that allows users to interact with a large language model in real time.

The system follows a client-server architecture where the frontend, developed using HTML, CSS, and JavaScript, communicates with a Flask backend through asynchronous HTTP requests. When a user submits a message, the frontend sends the input to the backend via a POST request. Flask receives the message, maintains the conversation history, and forwards the complete chat context to Groq's API. The LLaMA model generates a context-aware response, which is returned to the frontend in JSON format and displayed within the chat interface.

The chatbot preserves conversational continuity by storing both user and assistant messages, enabling multi-turn interactions. API credentials are managed securely using environment variables loaded through the python-dotenv package.

This project demonstrates the integration of modern Large Language Models (LLMs) into web applications while showcasing concepts such as RESTful communication, API integration, context management, JSON data exchange, and full-stack AI application development.
