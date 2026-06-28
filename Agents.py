# FIRST - get all libraries
from dotenv import load_dotenv
load_dotenv()

import os 
import requests

from langchain_mistralai import ChatMistralAI
from langchain.tools import tool

from langchain_core.messages import HumanMessage, ToolMessage

from tavily import TavilyClient


# SECOND - create tools 

# weather tool

@tool 
def weather(city : str) -> str :
    """ Get current weather in a city """
    api_key = os.getenv("OPENWEATHER_API_KEY")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    data = response.json()

    if str(data.get("cod")) != "200":
        return f"Error: data.get('message', 'Could not fetch weather')"

    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]

    return f"weather in {city.title()} is {temp}°C with {desc}. Humidity: {humidity}%. Wind: {wind_speed}km/h"

print(weather.invoke("Bhopal"))