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
def get_weather(city : str) -> str :
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

print(get_weather.invoke("Bhopal"))

# tavily news tool

tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))


@tool
def get_news(city: str) -> str:
    """Get latest news about the city."""

    response = tavily_client.search(
    query=f"Latest news about {city}",
    topic="news",
    search_depth="basic",
    max_results=5
)

    results = response.get("results", [])

    if not results:
        return f"No news found for {city}"

    news_list = []

    for r in results:
        title = r.get("title", "No title")
        url = r.get("url", "")
        snippet = r.get("content", "")

        news_list.append(
            f"- {title}\n"
            f"{url}\n"
            f"{snippet[:100]}..."
        )

    return f"Latest news for {city.title()}:\n\n" + "\n\n".join(news_list)

print(get_news.invoke("Bhopal"))


    
    

    