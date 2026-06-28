# ============================================================
#                    📰 NEWS TOOL
# ============================================================

import os

from tavily import TavilyClient
from langchain.tools import tool

# Create a Tavily client using the API key from the .env file
tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

@tool
def get_news(city: str) -> str:
    """
    Get the latest news for a city.
    
    Use this tool when the user asks about: 
    - today's news 
    - recent events
    - traffic disruptions
    - festivals
    - protests
    - road closures
    - public events
    """

    response = tavily_client.search(
    query=f"Latest news about {city}",
    topic="news",
    search_depth="basic",
    max_results=5
    )

    # Get the search results
    results = response.get("results", [])

    # If nothing is found
    if not results:
        return f"No news found for {city}."

    news_list = []

    # Loop through every news article
    for article in results:

        title = article.get("title", "No Title")
        url = article.get("url", "")
        snippet = article.get("content", "")

        news_list.append(
            f"- {title}\n"
            f"{url}\n"
            f"{snippet[:100]}..."
        )

    # Return all news articles
    return f"Latest news for {city.title()}:\n\n" + "\n\n".join(news_list)