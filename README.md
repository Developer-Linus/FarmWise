# FarmWise - AI-Powered Agricultural Assistant

FarmWise is an AI-powered chatbot designed to provide tailored agricultural advice to farmers, helping them make informed decisions, improve productivity, and adopt sustainable farming practices. The app is specifically designed to address the challenges faced by smallholder farmers in Kenya, offering affordable and accessible solutions.

---

## Key Features

- **Personalized Farming Advice**: AI-driven recommendations tailored to individual farmers based on their crops, soil conditions, and farming practices.
- **Localized Weather Updates**: Real-time weather forecasts and alerts to help farmers plan their activities effectively.
- **Learning Resources**: Access to tutorials, guides, and best practices for modern and sustainable farming techniques.
- **Pest and Disease Management**: Solutions to identify and manage pests and diseases affecting crops.
- **Data-Driven Insights**: Tools to analyze farm data and optimize planting, harvesting, and resource allocation.

---

## How It Works

1. **Register and Set Up Profile**: Farmers create an account and provide details about their location, crops, and farming practices.
2. **Chatbot Interaction**: Farmers ask questions or describe issues through the AI-powered chatbot, which provides tailored advice and solutions.
3. **Real-Time Weather Integration**: The app uses location data to deliver accurate weather forecasts and alerts.
4. **AI-Driven Insights**: The app analyzes user data and provides actionable recommendations for better farming outcomes.
5. **Continuous Learning**: Farmers can access a library of resources to improve their knowledge and skills.

---

## Installation and Setup

Follow these steps to set up the FarmWise app on your local machine:

### Prerequisites
- Python 3.8 or higher
- Flask
- nltk

### Installation Steps

1. **Clone the Repository**:
Open your Git bash or terminal
git clone https://github.com/Developer-Linus/FarmWise.git
```bash
cd FarmWise
```

3. **Install Dependencies**:
   Use `pip` to install the required Python libraries:
```bash
pip install -r requirements.txt
```
3. **Set Up the Database**:
   Initialize the SQLite database for storing user data and chatbot responses:
```bash
python setup_database.py
```
4. **Run the Application**:
   Start the Flask server:
```bash
python app.py
```

The app will be available at `http://127.0.0.1:5000`.


---

## Project Structure
```
FarmWise/
├── app.py                 # Main Flask application
├── chatbot/               # Chatbot logic and AI integration
│   ├── __init__.py
│   ├── train.py           # Training scripts for the chatbot
├── static/                # Static files (CSS, JavaScript, images)
├── templates/             # HTML templates for the frontend
├── intents.json       
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

---

## Usage

1. Open the app in your browser at `http://127.0.0.1:5000`.
2. Interact with the chatbot by typing your questions or issues in the chatbox.
3. Receive personalized farming advice, weather updates, and access to learning resources.

---

## Contributing

We welcome contributions to improve FarmWise! To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix:
   bash
git checkout -b feature-name
3. Commit your changes and push to your fork:
bash
git commit -m "Add feature-name"
git push origin feature-name
4. Open a pull request to the main repository.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact

For questions, feedback, or support, please contact us at **linusmksu30@gmail.com**.

---

## Future Plans

- Expand AI capabilities to support more crops and farming scenarios.
- Integrate multilingual support for better accessibility.
- Develop a mobile app for Android and iOS.
- Partner with agricultural organizations to provide additional resources and tools.
