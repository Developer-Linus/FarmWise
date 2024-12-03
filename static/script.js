// JavaScript for handling chat interactions
const chatBox = document.getElementById('chat-box');
const userInput = document.getElementById('user-input');
const sendButton = document.getElementById('send-button');

// Function to add a message to the chat
function addMessage(sender, message) {
    const messageElement = document.createElement('div');
    messageElement.classList.add('chat-message', sender);
    messageElement.textContent = message;
    chatBox.appendChild(messageElement);
    chatBox.scrollTop = chatBox.scrollHeight; // Auto-scroll to the latest message
}

// Event listener for the send button
sendButton.addEventListener('click', async () => {
    const message = userInput.value.trim();
    if (!message) return;

    // Add user message to chat
    addMessage('user', message);
    userInput.value = '';

    // Send message to backend and get response
    try {
        const response = await fetch('/chat', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message })
        });

        const data = await response.json();

        // Check if retraining is required
        if (data.retrain) {
            addMessage('bot', "Updating chatbot training data. Please wait...");
            await retrainChatbot();
            addMessage('bot', "Training complete! You can now continue chatting.");
        } else {
            addMessage('bot', data.response);
        }
    } catch (error) {
        addMessage('bot', 'Error: Unable to connect to the server.');
    }
});

// Allow pressing Enter to send a message
userInput.addEventListener('keypress', (event) => {
    if (event.key === 'Enter') {
        sendButton.click();
    }
});

// Function to retrain the chatbot (calls backend retrain endpoint)
async function retrainChatbot() {
    try {
        const response = await fetch('/retrain', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' }
        });
        if (!response.ok) throw new Error("Retraining failed.");
    } catch (error) {
        addMessage('bot', 'Error: Unable to retrain the chatbot.');
    }
}