# 🌍 City Intelligence Agent

An AI-powered City Intelligence Agent built using **LangChain**, **Mistral AI**, **Streamlit**, and **Tool Calling**. The agent can answer city-related questions by intelligently deciding when to use external tools such as Weather and News APIs.

---

## ✨ Features

* 🌤️ Real-time Weather Information
* 📰 Latest City News
* 🤖 AI Agent with Tool Calling
* 🧠 Conversation Memory
* 💬 Streamlit Chat Interface
* 📋 Human-in-the-Loop Tool Approval (Optional)
* 📝 Tool Call Logging
* ⚡ Clean and Modular Project Structure

---

## 🛠️ Tech Stack

### AI & LLM

* LangChain
* Mistral AI

### UI

* Streamlit

### APIs

* OpenWeather API
* Tavily Search API

### Python Libraries

* Requests
* Python Dotenv
* Rich

---

## 📂 Project Structure

```
Backend/
│
├── app.py                 # Streamlit application
├── agent.py               # AI Agent
│
├── tools/
│   ├── weather.py
│   └── news.py
│
├── middleware/
│   ├── approval.py
│   └── logger.py
│
├── prompts/
│   └── system_prompt.py
│
├── logs/
│   └── agent.log
│
├── .env
├── .env.example
├── requirements.txt
└── .gitignore
```

---

## 🚀 How It Works

```
User Question
      │
      ▼
Streamlit UI
      │
      ▼
LangChain Agent
      │
      ▼
Reasoning
      │
 ┌────┴────┐
 ▼         ▼
Weather   News
 Tool      Tool
 └────┬────┘
      ▼
Final AI Response
```

The agent first understands the user's question, decides whether external information is required, invokes the appropriate tool(s), and combines the results into a natural language response.

---

## 📸 Example Questions

* What's the weather in Delhi?
* Latest news about Mumbai.
* Is it a good day to visit Marine Drive?
* Should I carry an umbrella in Bangalore today?
* Is Jaipur a good place to visit this weekend?

---

## ⚙️ Installation

Clone the repository

```bash
git clone <repository-url>
```

Go to the project directory

```bash
cd Backend
```

Install dependencies

```bash
python -m pip install -r requirements.txt
```

Create a `.env` file

```env
MISTRAL_API_KEY=your_key
OPENWEATHER_API_KEY=your_key
TAVILY_API_KEY=your_key
```

Run the application

```bash
python -m streamlit run app.py
```

---

## 🧠 Concepts Practiced

* AI Agents
* Tool Calling
* Prompt Engineering
* Conversation Memory
* Middleware
* Modular Python Project Structure
* Streamlit
* Environment Variables
* API Integration

---

## 🎯 Future Improvements

* Location-based recommendations
* Maps Integration
* Multi-tool reasoning
* Restaurant Finder
* Hotel Recommendations
* Travel Planner
* Event Discovery
* AI-generated Trip Itineraries

---

## 👨‍💻 Author

Built as a project to learn **Generative AI**, **AI Agents**, **LangChain**, and **LLM Application Development** through project-based learning.
