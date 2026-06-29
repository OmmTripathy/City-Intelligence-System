<div align="center">

# 🌍 City Intelligence Agent

> An AI agent that answers city-related questions using real-time weather and news —
> powered by LangChain tool calling and Mistral AI.

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://city-intelligence-system-p6qw8lft9ob4lc6pku97jy.streamlit.app/)

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=flat-square&logo=langchain&logoColor=white)
![LangGraph](https://img.shields.io/badge/LangGraph-1C3C3C?style=flat-square&logo=langchain&logoColor=white)
![Mistral AI](https://img.shields.io/badge/Mistral_AI-FF7000?style=flat-square)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)

</div>

---

## 🚀 Live Demo

**Try it now →** [city-intelligence-system-p6qw8lft9ob4lc6pku97jy.streamlit.app](https://city-intelligence-system-p6qw8lft9ob4lc6pku97jy.streamlit.app/)

> No setup needed. Ask about any city's weather, news, or weekend plans — the agent reasons and responds in real time.

---

## What It Does

Ask the agent anything about a city — it reasons about whether it needs live data,
calls the right tool (weather or news), and returns a grounded natural language response.

```
"Should I carry an umbrella in Bangalore today?"
"Latest news about Mumbai."
"Is it a good weekend to visit Jaipur?"
```

No hardcoded answers. The agent decides what to look up and when.

---

## How It Works

```
User Question → Streamlit UI → LangChain Agent → Reasoning
                                                      │
                                            ┌─────────┴─────────┐
                                            ▼                   ▼
                                       Weather Tool         News Tool
                                       (OpenWeather)        (Tavily)
                                            └─────────┬─────────┘
                                                      ▼
                                              Final AI Response
```

---

## 🧠 GenAI / LLM Stack

| Component | Tool | Link |
|---|---|---|
| LLM | Mistral AI (`mistral-small-2506`) | [mistral.ai/technology](https://mistral.ai/technology/) |
| Agent Loop | LangGraph `create_react_agent` (ReAct) | [langgraph docs](https://langchain-ai.github.io/langgraph/) |
| Tool Calling | LangChain Tools (`@tool`) | [langchain tool calling](https://python.langchain.com/docs/concepts/tool_calling/) |
| Conversation Memory | LangGraph `InMemorySaver` (checkpointer) | [langgraph memory](https://langchain-ai.github.io/langgraph/concepts/memory/) |
| Observability | LangChain `BaseCallbackHandler` | [langchain callbacks](https://python.langchain.com/docs/concepts/callbacks/) |
| Weather Data | OpenWeatherMap API | [openweathermap.org](https://openweathermap.org/api) |
| News & Search | Tavily Search API | [tavily.com](https://tavily.com/) |

> **ReAct loop:** The agent reasons step-by-step — calling `get_weather`, observing the result, then calling `get_news`, observing that — before synthesizing a final combined answer. This is how "should I visit X this weekend?" triggers both tools automatically.

---

## Tech Stack

| Layer | Technology |
|---|---|
| LLM | [Mistral AI](https://mistral.ai) |
| Agent Framework | [LangChain](https://python.langchain.com) + [LangGraph](https://langchain-ai.github.io/langgraph/) |
| UI | [Streamlit](https://streamlit.io) |
| Weather Data | [OpenWeather API](https://openweathermap.org/api) |
| News & Search | [Tavily Search API](https://tavily.com) |
| Language | Python 3.10+ |

---

## Key Concepts Implemented

- **Tool Calling** — agent dynamically decides which tools to invoke based on the query
- **Conversation Memory** — context retained across turns via LangGraph `InMemorySaver` + `thread_id`
- **Prompt Engineering** — custom system prompt shaping agent reasoning and multi-tool behavior
- **Middleware / Callbacks** — structured tool call logging via `BaseCallbackHandler`
- **Modular Architecture** — tools, prompts, middleware cleanly separated

---

## Project Structure

```
Backend/
├── app.py                 # Streamlit UI
├── agent.py               # LangGraph ReAct agent setup
├── tools/
│   ├── weather.py         # OpenWeather tool
│   └── news.py            # Tavily search tool
├── middleware/
│   ├── approval.py        # Human-in-the-loop approval
│   └── logger.py          # Tool call logging (BaseCallbackHandler)
├── prompts/
│   └── system_prompt.py   # Agent system prompt
├── logs/
│   └── agent.log
├── .env.example
├── requirements.txt
└── .gitignore
```

---

## Setup

```bash
# Clone the repo
git clone <repository-url>
cd Backend

# Install dependencies
pip install -r requirements.txt

# Configure environment variables
cp .env.example .env
```

Add your keys to `.env`:

```env
MISTRAL_API_KEY=your_key
OPENWEATHER_API_KEY=your_key
TAVILY_API_KEY=your_key
```

Run the app:

```bash
streamlit run app.py
```

---

## Example Queries

| Query | Tools Invoked |
|---|---|
| "Will it rain in Delhi tomorrow?" | `get_weather` |
| "What's happening in Chennai this week?" | `get_news` |
| "Should I visit Goa this weekend?" | `get_weather` + `get_news` |
| "Is it a good day to go out in Pune?" | `get_weather` + `get_news` |
| "How about Hyderabad?" *(follow-up)* | Memory → infers city → tools |

---

## Author

**Omm Kishor Tripathy** — [LinkedIn](https://linkedin.com/in/ommtripathy) · [GitHub](https://github.com/OmmTripathy)

---

<div align="center">
  <sub>Built with LangGraph · Mistral AI · Streamlit</sub>
</div>
