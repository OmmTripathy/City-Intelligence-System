<div align="center">

# 🌍 City Intelligence Agent

> An AI agent that answers city-related questions using real-time weather and news —
> powered by LangChain tool calling and Mistral AI.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=flat-square&logo=langchain&logoColor=white)
![Mistral AI](https://img.shields.io/badge/Mistral_AI-FF7000?style=flat-square)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)

</div>

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

## Tech Stack

| Layer | Technology |
|---|---|
| LLM | Mistral AI |
| Agent Framework | LangChain |
| UI | Streamlit |
| Weather Data | OpenWeather API |
| News & Search | Tavily Search API |
| Language | Python |

---

## Key Concepts Implemented

- **Tool Calling** — agent dynamically decides which tools to invoke based on the query
- **Conversation Memory** — context retained across turns in the same session
- **Prompt Engineering** — custom system prompt shaping agent reasoning behavior
- **Middleware Layer** — optional human-in-the-loop tool approval + structured logging
- **Modular Architecture** — tools, prompts, middleware cleanly separated

---

## Project Structure

```
Backend/
├── app.py                 # Streamlit UI
├── agent.py               # LangChain agent setup
├── tools/
│   ├── weather.py         # OpenWeather tool
│   └── news.py            # Tavily search tool
├── middleware/
│   ├── approval.py        # Human-in-the-loop approval
│   └── logger.py          # Tool call logging
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

## Roadmap

- [ ] Maps integration
- [ ] Multi-tool reasoning chains
- [ ] Restaurant and hotel recommendations
- [ ] AI-generated trip itineraries
- [ ] Event discovery by city
