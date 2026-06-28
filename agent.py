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


# Import the News Tool
from tools.news import get_news


# Used to store conversation history in memory
from langgraph.checkpoint.memory import InMemorySaver
memory = InMemorySaver()


llm = ChatMistralAI(
    model = "mistral-small-2506",
    api_key = os.getenv("MISTRAL_API_KEY")
)


# Import human approval
from middleware.approval import human_approval

SYSTEM_PROMPT = """
You are a City Intelligence Agent.

Your job is to help users with city-related questions.

Guidelines:

1. Use the Weather Tool for any weather-related question.
2. Use the News Tool for any latest or recent news.
3. Never make up weather or news information.
4. If a tool returns an error, clearly tell the user.
5. Be polite and professional.
6. Keep answers short and easy to understand.
7. If the user asks a general knowledge question, answer it directly without using tools.
"""

agent = create_agent(
    llm,
    tools = [get_weather,get_news],
    system_prompt= SYSTEM_PROMPT,
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
