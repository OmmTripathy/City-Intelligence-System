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

First reasoning about what information is needed, 
then use the available tools for any real-time information (such as weather or recent news), 
using one or multiple tools whenever required to provide the most accurate recommendation; 
never guess current information, answer general knowledge questions directly without tools, 
clearly communicate tool errors, and keep responses concise, clear, and easy to understand.
"""

# Every time the agent runs, save information like: what is que, what time , which tool used, final answer.
from middleware.logger import tool_logger

agent = create_agent(
    llm,
    tools = [get_weather,get_news],
    system_prompt= SYSTEM_PROMPT,
    middleware= [tool_logger, human_approval],
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
