# backend/app.py

from flask import Flask, jsonify, request
from chatbot.bot import get_response
from flask_cors import CORS
from database.models import init_db

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
  return jsonify({"message": "Welcome to FarmWise API!"})

@app.route('/chat', methods=['POST'])
def chat():
  """
  Endpoint to interact with the chatbot.
  Expects a JSON payload with a 'message' field.
  """
  data = request.get_json()
  user_input = data.get('message', '')
  response = get_response(user_input)
  return jsonify({"response": response})

if __name__ == '__main__':
  app.run(debug=True)