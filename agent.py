from dotenv import load_dotenv
load_dotenv()

import os 
import requests

from langchain_mistralai import ChatMistralAI
from langchain.tools import tool
from rich import print
from langchain.agents import create_agent



# Import the Weather Tool
from tools.weather import get_weather

print(get_weather.invoke("Bhopal"))

# Import the News Tool
from tools.news import get_news

print(get_news.invoke("Bhopal"))

# Import Human approval 
from middleware.approval import human_approval


