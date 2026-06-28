


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


# Import the Weather Tool
from tools.weather import get_weather

print(get_weather.invoke("Bhopal"))

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

