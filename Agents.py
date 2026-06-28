# FIRST - get all libraries
from dotenv import load_dotenv
load_dotenv()

import os 
import requests

from langchain_mistralai import ChatMistralAI
from langchain.tools import tool
from langchain_core.messages import HumanMessage, ToolMessage
from tavily import TavilyClient
from rich import print
from langchain.agents import create_agent
from langchain.agents.middleware import wrap_tool_call

# SECOND - create tools 

# ============================================================
#                 🌦️ WEATHER TOOL
# ============================================================
@tool 
def get_weather(city : str) -> str :
    """ Get current weather in a city """
    api_key = os.getenv("OPENWEATHER_API_KEY")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    data = response.json()

    if data.get("cod") != 200:
        return f"Error: {data.get('message', 'Could not fetch weather')}"

    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]

    return f"weather in {city.title()} is {temp}°C with {desc}. Humidity: {humidity}%. Wind: {wind_speed}km/h"


# ============================================================
#                    📰 NEWS TOOL
# ============================================================

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

# ============================================================
#                 🧠 LLM INITIALIZATION
# ============================================================

llm = ChatMistralAI(
    model = "mistral-small-2506",
    api_key = os.getenv("MISTRAL_API_KEY")
)

@wrap_tool_call
def human_approval(request, handler):
    """Ask for human approval before every tool call."""

    tool_name = request.tool_call["name"]

    confirm = input(f"Agent wants to call '{tool_name}'. Approve? (y/n): ")

    if confirm.lower() not in ["y", "yes"]:
        return ToolMessage(
            content="Tool call denied by user.",
            tool_call_id=request.tool_call["id"]
        )

    return handler(request)

agent = create_agent(
    llm,
    tools = [get_weather,get_news],
    system_prompt= "you are a helpful city assistant.",
    middleware= [human_approval]
)

print("City Agent | type exit to quit")

while True:
    user_input = input("You : ")
    if user_input.lower() == "exit":
        break 
    result = agent.invoke({
        "messages": [{"role": "user", "content": user_input}]
    })

    print("bot : ", result['messages'][-1].content )