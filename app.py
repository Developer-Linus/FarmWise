from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import nltk
from nltk.chat.util import Chat, reflections
import os

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing for frontend-backend communication

# Download necessary NLTK data (if not already downloaded)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Define pairs of input-output for the chatbot using NLTK
pairs = [
    (r"Hi|Hello", ["Hello! How can I assist you with farming today?"]),
    (r"How are you?", ["I'm good, thanks for asking! How can I help you with farming?"]),
    (r"(.*) weather (.*)", ["The weather is important for farming. Please check local weather forecasts."]),
    (r"(.*) crops (.*)", ["There are many crops you can grow. What type of crops are you interested in?"]),
    (r"(.*) pests (.*)", ["Pest control is crucial. Have you tried organic methods or chemicals for pest control?"]),
    (r"quit", ["Goodbye! Feel free to come back anytime."])
]

# Create the chatbot using NLTK's Chat class
chatbot = Chat(pairs, reflections)

# Route: Home Page
@app.route('/')
def home():
    """
    Render the home page with the chatbot interface.
    """
    return render_template('index.html')

# Route: Chat API
@app.route('/chat', methods=['POST'])
def chat():
    """
    Handle user input and return chatbot response.
    """
    try:
        data = request.get_json()
        user_input = data.get('message', '')
        if not user_input:
            return jsonify({"response": "Please enter a valid message."}), 400

        # Get response from ChatBot (using NLTK's chatbot)
        response = chatbot.respond(user_input)
        if not response:
            response = "Sorry, I didn't understand that. Can you rephrase?"

        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)