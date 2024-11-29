# backend/chatbot/bot.py

from ai.rules import generate_advice

def get_response(user_input):
  """
  Generate a response based on user input.
  For now, it uses a simple rule-based AI logic.
  """
  # Example: Parse user input to extract relevant information
  # This is a placeholder for actual parsing logic
  crop_type = "wheat"
  soil_condition = "loamy"
  weather = "sunny"

  # Generate advice using AI logic
  advice = generate_advice(crop_type, soil_condition, weather)
  return advice