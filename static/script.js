//user types → clicks Send → sendMessage() runs
// → reads the typed text → shows it immediately in the chat box 
// → clears the input → sends it to Flask via POST request
//  → waits for Flask to call Groq API and return a reply 
// → displays the reply in the chat box → scrolls to bottom
async function sendMessage() {
    let input=
    document.getElementById("user-input");
    let message=input.value;
    if (message.trim()=="")return;
    let chatBox=
    document.getElementById("chat-box");
    //show user message
    chatBox.innerHTML+=`<div class="user">
            <b>You:</b> ${message}</div>`;
    input.value="";
    // send request to Flask backend
    const response=await fetch("/chat",{
        method:"POST",
        headers: {
            "Content-Type":"application/json"
        },
        body: JSON.stringify({message})
    });
    const data=await response.json();
    //show bot response
    chatBox.innerHTML+=`<div class="bot"><b>Bot:</b>${data.reply}</div>`
    //auto scroll
    chatBox.scrollTop=chatBox.scrollHeight;
    
}