# 🤖 AI Agents with Phidata & Groq

A collection of AI agent projects built using [Phidata](https://docs.phidata.com/) and [Groq](https://groq.com/), progressing from a simple single agent to a multi-agent AI stock analyst team.

---

## 💡 Project Overview

This project demonstrates how to build AI agents that can think, use tools, and work together to answer complex real-world questions — in this case, analysing stocks and delivering investment insights.

The three files are structured as a learning progression:

| File | Description |
|------|-------------|
| `1_simple_groq_agent.py` | A basic AI agent that responds to a prompt |
| `2_finance_agent.py` | An agent with access to live financial data tools |
| `3_agent_teams.py` | A team of specialised agents acting as an AI stock analyst |

---

## 🛠️ Technologies Used

- **[Phidata](https://docs.phidata.com/)** — Framework for building AI agents and agent teams
- **[Groq](https://groq.com/)** — LLM provider running Llama 3.3 70B (fast inference)
- **[YFinance](https://pypi.org/project/yfinance/)** — Fetches live stock data from Yahoo Finance
- **[DuckDuckGo Search](https://pypi.org/project/duckduckgo-search/)** — Web search tool for retrieving latest news
- **Python-dotenv** — Manages API keys securely via a `.env` file

---

## 📁 File Breakdown

### `1_simple_groq_agent.py` — Basic Agent
The simplest possible AI agent. It connects to Groq's Llama 3.3 70B model and responds to a single prompt.

**Purpose:** Demonstrates how to set up an agent with just a few lines of code.

**Expected Output:**
```
In a golden bowl they met one day,
Dosa crisp, Samosa here to stay.
```

---

### `2_finance_agent.py` — Finance Agent
An agent equipped with financial data tools. It can look up live stock prices, analyst recommendations, and company fundamentals from Yahoo Finance.

**Purpose:** Demonstrates how to give an AI agent access to real-world data tools.

**Expected Output:**
```
## TSLA vs Phidata — Analyst Summary

| Metric         | TSLA         |
|----------------|--------------|
| Current Price  | $XXX.XX      |
| Recommendation | Hold/Buy/Sell|
| PE Ratio       | XX.X         |
...
```

---

### `3_agent_teams.py` — AI Stock Analyst Team ⭐
The most advanced file. Two specialised agents work together as a team:

- **Web Agent** — Searches the web for the latest news on a stock (using DuckDuckGo)
- **Finance Agent** — Pulls live financial data and analyst recommendations (using YFinance)

Together they act as an **AI-powered stock analyst**, combining real-time news with financial data to give a comprehensive view of a stock (in this case, NVIDIA).

**Purpose:** Demonstrates multi-agent collaboration, where each agent has a defined role and they work together to answer a complex question.

**Expected Output:**
```
## NVDA — Analyst Recommendations

| Firm         | Rating | Price Target |
|--------------|--------|--------------|
| Morgan Stanley | Buy  | $XXX         |
| Goldman Sachs  | Hold | $XXX         |
...

## Latest News
- [Source] NVIDIA announces new AI chip...
- [Source] NVDA beats earnings expectations...
```

---

## ⚙️ Setup & Installation

### 1. Clone the repo
```bash
git clone https://github.com/LinusLimJingXian/Projects.git
cd Projects
```

### 2. Install dependencies
```bash
pip install phidata groq yfinance duckduckgo-search python-dotenv
```

### 3. Set up your API keys
Create a `.env` file in the project root:
```
GROQ_API_KEY=your_groq_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
```
> Get your free Groq API key at [console.groq.com](https://console.groq.com)

### 4. Run any file
```bash
python 1_simple_groq_agent.py
python 2_finance_agent.py
python 3_agent_teams.py
```

---

## 🔒 Security Note

API keys are stored in a `.env` file which is excluded from version control via `.gitignore`. Never commit your `.env` file to GitHub.

---

## 📌 Key Concepts Demonstrated

- **AI Agents** — Autonomous programs that use LLMs to reason and take actions
- **Tool Use** — Giving agents access to external data sources (web, finance APIs)
- **Multi-Agent Systems** — Multiple specialised agents collaborating to solve complex tasks
- **Prompt Engineering** — Giving agents clear instructions to format and present data effectively
