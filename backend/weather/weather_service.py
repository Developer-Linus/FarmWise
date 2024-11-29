# backend/weather/weather_service.py

import requests

def get_weather(location):
  """
  Fetch weather data for a given location using a weather API.
  """
  # TODO: Replace with actual API key and endpoint
  api_key = "YOUR_API_KEY"
  endpoint = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"

  response = requests.get(endpoint)
  if response.status_code == 200:
      data = response.json()
      # Extract relevant weather information
      weather_description = data['weather'][0]['description']
      return weather_description
  else:
      return "Unable to fetch weather data"