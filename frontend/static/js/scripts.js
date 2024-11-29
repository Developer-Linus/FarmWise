// frontend/static/js/scripts.js

document.addEventListener('DOMContentLoaded', function() {
    const chatForm = document.getElementById('chat-form');
    const chatBox = document.getElementById('chat-box');
    const userInput = document.getElementById('user-input');
  
    chatForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const message = userInput.value.trim();
        if (message) {
            appendMessage('You', message);
            userInput.value = '';
  
            // Send the message to the server
            fetch('http://localhost:5000/chat', { // Ensure the correct backend URL
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json', // Use JSON
                },
                body: JSON.stringify({ 'message': message }) // Use JSON.stringify
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                return response.json();
            })
            .then(data => {
                appendMessage('FarmWise', data.response);
            })
            .catch(error => {
                console.error('Error:', error);
                appendMessage('FarmWise', 'Sorry, something went wrong.');
            });
        }
    });
  
    function appendMessage(sender, message) {
        const messageElement = document.createElement('div');
        messageElement.textContent = `${sender}: ${message}`;
        chatBox.appendChild(messageElement);
        chatBox.scrollTop = chatBox.scrollHeight;
    }
  });