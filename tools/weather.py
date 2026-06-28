# ============================================================
#                 🌦️ WEATHER TOOL
# ============================================================

import os 
import requests

from langchain.tools import tool

@tool 
def get_weather(city : str) -> str :
    """ Get current weather in a city """

    # Read API key from the .env file
    api_key = os.getenv("OPENWEATHER_API_KEY")

    # OpenWeather API URL
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    # Send request to the API
    response = requests.get(url)
    
    # Convert JSON response into a Python dictionary
    data = response.json()

    # Check if the API returned an error
    if data.get("cod") != 200:
        return f"Error: {data.get('message', 'Could not fetch weather')}"

    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]

    return (
        f"Weather in {city.title()} is {temp}°C with {desc}. "
        f"Humidity: {humidity}%. "
        f"Wind: {wind_speed} km/h."
    )