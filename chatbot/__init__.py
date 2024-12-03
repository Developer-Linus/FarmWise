import os
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import random
import json

# Ensure required NLTK packages are downloaded
nltk.download("punkt")  # For tokenization
nltk.download("stopwords")  # For stop words (optional)

# Define intents and responses (can be moved to a JSON file for scalability)
intents_file = "intents.json"  # Path to your intents file

if os.path.exists(intents_file):
    with open(intents_file, "r") as f:
        intents_data = json.load(f)
else:
    raise FileNotFoundError(f"The file {intents_file} was not found. Ensure you have an intents.json file.")

# Function to classify user input into intents
def classify_intent(user_input):
    """
    Classifies the user's input to determine the intent.

    Args:
        user_input (str): The user's message.
    
    Returns:
        str: The classified intent or 'unknown' if no match is found.
    """
    tokens = word_tokenize(user_input.lower())  # Tokenize the user input
    for intent in intents_data["intents"]:
        if any(keyword in tokens for keyword in intent["keywords"]):
            return intent["tag"]
    return "unknown"  # Default if no matching intent is found

# Function to generate a response based on the classified intent
def get_response(intent):
    """
    Retrieves a response based on the identified intent.

    Args:
        intent (str): The classified intent.

    Returns:
        str: A random response from the corresponding intent's responses.
    """
    for intent_data in intents_data["intents"]:
        if intent_data["tag"] == intent:
            return random.choice(intent_data["responses"])
    return "I'm sorry, I don't understand that."  # Default response for unknown intents

# Function to train (or initialize) the chatbot
def train_chatbot():
    """
    Placeholder function for training logic.
    In this example, the chatbot is initialized using predefined intents from a JSON file.
    """
    print("Initializing the chatbot with predefined intents...")
    # In this case, 'training' just ensures the intents file is loaded.
    print("Chatbot training complete. Ready to chat!")

# Check if the intents file exists; if not, notify the user
if not os.path.exists(intents_file):
    raise FileNotFoundError(f"The file {intents_file} was not found. Create an intents.json file to train the chatbot.")
else:
    train_chatbot()
