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

# ============================================================
#                  WEATHER TOOL
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
#                     NEWS TOOL
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
#                  LLM INITIALIZATION
# ============================================================

llm = ChatMistralAI(
    model = "mistral-small-2506",
    api_key = os.getenv("MISTRAL_API_KEY")
)

tools = {
    "get_weather": get_weather,
    "get_news": get_news
}

llm_with_tool = llm.bind_tools([get_weather, get_news])
    

# ============================================================
#                   AGENT LOOP
# ============================================================

messages = []

print("City Intelligent System")
print("Type exit to quit")

while True: 
    user_input = input("You : ")
    if user_input.lower() == "exit":
        break

    messages.append(HumanMessage(content = user_input))

    while True:
        result = llm_with_tool.invoke(messages)
        messages.append(result)

        if result.tool_calls:
            denied = False

            for tool_call in result.tool_calls:

                tool_name = tool_call["name"]

                # HUMAN IN THE LOOP
                confirm = input(f"Agent wants to call '{tool_name}' → Approve? (y/n): ")

                if confirm.lower() in ["n", "no"]:
                    print("Tool call denied. I cannot get the latest information.")
                    denied = True
                    break

                # Execute tool
                tool_result = tools[tool_name].invoke(tool_call["args"])

                messages.append(ToolMessage(
                        content=tool_result,
                        tool_call_id=tool_call["id"]
                    ))

            if denied:
                break

            continue

        else:
            print("\nFinal Answer:\n")
            print(result.content)
            break


