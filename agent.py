from dotenv import load_dotenv
load_dotenv()

import os
from langchain_mistralai import ChatMistralAI
from rich import print
from langgraph.prebuilt import create_react_agent   # FIX 1: correct import
from langgraph.checkpoint.memory import InMemorySaver

from tools.weather import get_weather
from tools.news import get_news
from middleware.logger import tool_logger

memory = InMemorySaver()

llm = ChatMistralAI(
    model="mistral-small-2506",
    api_key=os.getenv("MISTRAL_API_KEY")
)

SYSTEM_PROMPT = """
You are a City Intelligence Agent.
Your job is to help users with city-related questions.

Rules:
- Always consider the previous conversation before answering.
- If the user asks a follow-up like "Is it good to go out?", "How about tomorrow?",
  or "Should I carry an umbrella?", infer the city from the conversation history.
- If recent weather data is already in the conversation, reuse it unless the user
  asks for updated info.
- Never claim you lack access to weather or news — tools are always available.
- For any trip planning or "should I go out / visit" query, ALWAYS call BOTH the
  weather tool AND the news tool for that city, then combine both results into a
  single coherent answer covering conditions and relevant local happenings.
- Answer concisely.
"""

agent = create_react_agent(     # FIX 2 & 3: correct function + correct param name
    llm,
    tools=[get_weather, get_news],
    prompt=SYSTEM_PROMPT,
    checkpointer=memory
)

THREAD_ID = "city-chat"

def chat_with_agent(user_input: str, thread_id: str = THREAD_ID) -> str:
    result = agent.invoke(
        {"messages": [{"role": "user", "content": user_input}]},
        config={
            "configurable": {"thread_id": thread_id},
            "callbacks": [tool_logger]      # FIX 4: middleware goes here
        }
    )
    return result["messages"][-1].content

if __name__ == "__main__":
    print("City Agent | Type 'exit' to quit.\n")
    while True:
        user_input = input("You : ")
        if user_input.lower() == "exit":
            break
        response = chat_with_agent(user_input)
        print("Bot :", response)