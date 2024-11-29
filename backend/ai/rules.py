# backend/ai/rules.py

def generate_advice(crop_type, soil_condition, weather):
  """
  Generate farming advice based on crop type, soil condition, and weather.
  This is a simple rule-based implementation.
  """
  # TODO: Implement more complex logic
  advice = f"For {crop_type} with {soil_condition} soil and {weather} weather, consider regular irrigation."
  return advice