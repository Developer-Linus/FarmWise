import json
import os
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import random
import pickle
from . import chatbot  # Import the chatbot instance from __init__.py

def retrain_chatbot():
    """
    Retrain the chatbot using the intents JSON file.
    This script updates the chatbot's training data with new information.
    """
    intents_file = "intents.json"
    model_file = "model.pkl"
    stop_words = set(stopwords.words("english"))

    def preprocess_data(intents):
        """
        Preprocess intents data into training data.
        """
        words = []
        classes = []
        training_data = []

        for intent in intents["intents"]:
            for pattern in intent["keywords"]:
                # Tokenize words and filter stop words
                tokenized_words = word_tokenize(pattern)
                words.extend(tokenized_words)

                # Add to training data
                training_data.append((tokenized_words, intent["tag"]))

            if intent["tag"] not in classes:
                classes.append(intent["tag"])

        words = sorted(set([w.lower() for w in words if w not in stop_words]))
        classes = sorted(set(classes))
        return words, classes, training_data

    def train_model():
        """
        Train the chatbot model with the current intents data.
        """
        # Load intents file
        if not os.path.exists(intents_file):
            print(f"Error: '{intents_file}' not found.")
            return

        with open(intents_file, "r") as file:
            intents = json.load(file)

        # Preprocess data
        words, classes, training_data = preprocess_data(intents)

        # Save the model
        with open(model_file, "wb") as file:
            pickle.dump((words, classes, training_data), file)

        print("Chatbot retrained and model saved successfully!")

    print("Retraining the chatbot with the latest intents...")
    train_model()
    print("Retraining complete!")

if __name__ == "__main__":
    retrain_chatbot()