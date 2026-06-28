# ============================================================
#                 🌦️ WEATHER TOOL
# ============================================================

import os 
import requests

from langchain.tools import tool

@tool 
def get_weather(city : str) -> str :
    """ 
    Get the current weather for a city.

    Use this tool when the user asks about:
    - weather
    - rain
    - temperature
    - humidity
    - outdoor activities
    - sightseeing
    - travel planning
    """

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
    feels_like = data["main"]["feels_like"]
    desc = data["weather"][0]["description"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    cloud_cover = data["clouds"]["all"]
    visibility = data["visibility"]

    return (
    f"📍 City: {city.title()}\n\n"
    f"🌡 Temperature: {temp}°C\n"
    f"🤗 Feels Like: {feels_like}°C\n"
    f"☁ Weather: {desc.title()}\n"
    f"💧 Humidity: {humidity}%\n"
    f"💨 Wind Speed: {wind_speed} m/s\n"
    f"👀 Visibility: {visibility / 1000:.1f} km\n"
    f"☁ Cloud Cover: {cloud_cover}%"
)