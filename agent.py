from dotenv import load_dotenv
load_dotenv()

import os 
import requests

from langchain_mistralai import ChatMistralAI
from langchain.tools import tool
from rich import print
from langchain.agents import create_agent

# Used to store conversation history in memory
from langgraph.checkpoint.memory import InMemorySaver

memory = InMemorySaver()

# Import the Weather Tool
from tools.weather import get_weather

print(get_weather.invoke("Bhopal"))

# Import the News Tool
from tools.news import get_news

print(get_news.invoke("Bhopal"))


llm = ChatMistralAI(
    model = "mistral-small-2506",
    api_key = os.getenv("MISTRAL_API_KEY")
)

# Import human approval
from middleware.approval import human_approval

agent = create_agent(
    llm,
    tools = [get_weather,get_news],
    system_prompt= "you are a helpful city assistant.",
    middleware= [human_approval],
    checkpointer=memory
)

print("City Agent | type exit to quit")

while True:
    user_input = input("You : ")
    if user_input.lower() == "exit":
        break 
    result = agent.invoke(
    {"messages": [{
                "role": "user",
                "content": user_input
            }]
    },
    # Keep using the same conversation
    config={"configurable": {"thread_id": "city-chat"}})

    print("bot : ", result['messages'][-1].content )
