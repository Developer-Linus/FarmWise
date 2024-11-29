# frontend/app.py

from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

# Route for the homepage
@app.route('/')
def index():
  return render_template('index.html')

# Route to handle chat messages
@app.route('/send_message', methods=['POST'])
def send_message():
  user_message = request.form['message']
  # Send the message to the backend API
  response = requests.post('http://localhost:5000/chat', json={'message': user_message})
  bot_response = response.json().get('response', 'Sorry, something went wrong.')
  return jsonify({'response': bot_response})

if __name__ == '__main__':
  app.run(port=5001, debug=True)