"""
 user types a message in the browser → JavaScript sends a POST request to /chat with the message
 → Flask receives it, adds it to history, sends the full history to Groq API → Groq's LLaMA model generates a reply 
 → reply gets added to history and sent back to the browser as JSON → JavaScript displays it in the chat UI
"""
from flask import Flask,render_template,request,jsonify
#flask ---Create web application
#render_template--->render html template
#request-->receives frontend data and sends to backend
#jsonify--->converts python object into json format
from groq import Groq
from dotenv import load_dotenv
#Used to load the API_KEY from the .env file
#To access environment variables ,importing OS
import os
load_dotenv() 
#Reads the hidden env variables from .env file
#Flask app initialization
app = Flask(__name__)
#Connecting groq api key to client through OS
#initialize groq client
client=Groq(api_key=os.getenv("GROQ_API_KEY"))
#To store the chat history
chat_history=[]
#To render the template
@app.route("/")
def home():
    return render_template("index.html")
#@app.route("/") maps the root URL (localhost:5000/) to the home() function.
#When someone opens the app in a browser, Flask serves index.html from the templates/ folder.
#This is the chatbot's frontend page
@app.route("/chat",methods=["POST"])
#This route handles POST requests to localhost:5000/chat
#When the user submits a message from the frontend
#the JavaScript sends a POST request here with the message data.
def chat():
    #Receive JSON data
    data=request.json
    #request.json parses the JSON body sent from the frontend. 
    #data["message"] extracts just the user's typed text from that JSON object 
    #— expects the frontend to send something like {"message": "Hello"}.
    #Extract the user message
    user_message=data["message"]
    #user message linked to history
    #Send the user message to Groq and get 
    #Add user message to history
    #Adds the user's message to chat_history in the format the Groq/LLaMA API 
    #expects — a dictionary with "role" (who sent it: "user" or "assistant")
    #and "content" (the actual text).
    chat_history.append({
        "role":"user",
        "content":user_message
    })
    
    #Sends request to Groq API 
    #Sends the entire chat_history (not just the latest message — the whole conversation so far) to Groq's API,running the LLaMA 3.3 70B model.
    #temperature=0.7 controls randomness/creativity (0 = deterministic/robotic, 1 = very creative/unpredictable, 0.7 is a balanced middle ground). 
    #max_tokens=1024 caps the response length at 1024 tokens.
    completion=client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=chat_history,
        temperature=0.7,
        max_tokens=1024
    )
    
    #Extracts the actual text response from the API's return object. 
    #.choices[0] gets the first (and usually only) completion generated
    #.message.content gets the text string from it.
    bot_reply=completion.choices[0].message.content
    
    #Stores the bot's reply in history
    #so next time the user sends a message
    #the API sees both sides of the conversation (user messages AND assistant replies)
    #giving it full context to respond appropriately.
    chat_history.append({
        "role":"assistant",
        "content":bot_reply
    })
    
    #Send response to frontend
    #Sends the bot's response back to the frontend as JSON: {"reply": "the bot's answer here"}.
    #The frontend JavaScript will receive this and display it in the chat UI.
    return jsonify({
        "reply":bot_reply
    })
if (__name__=="__main__"):   #to deploy and run the python file
    app.run(debug=True)    
    #if __name__ == "__main__" ensures this only runs when you execute this file directly (not when it's imported as a module elsewhere). 
    #app.run(debug=True) starts the Flask development server — debug=True enables auto-reload (server restarts automatically when you save code changes)
    #shows detailed error messages in the browser, useful during development.
     
     
    
    
    




