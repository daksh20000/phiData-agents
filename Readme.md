# 🧠 Multi-Agent AI System with PHI, Gemini, and Groq

This project demonstrates a multi-agent system using the [PHI](https://github.com/typetheta/phi) framework. It integrates Google's **Gemini**, **Groq** models, and various tools for **financial analysis**, **web scraping**, and **multi-agent collaboration**.

---

## 🚀 Features

- 🔍 **Financial Analysis Agent**
  - Uses Gemini model
  - Integrated with `YFinanceTools` to fetch:
    - ✅ Stock prices
    - ✅ Analyst recommendations
    - ✅ Stock fundamentals
  - Outputs data in **markdown tables**

- 🌐 **Web Scraping Agent**
  - Powered by Gemini or Groq models
  - Uses `Crawl4aiTools` and `WebsiteTools`
  - Scrapes and summarizes web content

- 🤖 **Team Agent Collaboration**
  - Coordinates multiple agents (`webAgent`, `financeAgent`)
  - Combines results with markdown formatting and cited sources

---

## 🧠 Agents Overview

### 📊 Finance Agent
```python
from phi.agent import Agent
from phi.model.google import Gemini
from phi.tools.yfinance import YFinanceTools

financeAgent = Agent(
    model=Gemini(id="gemini-1.5-flash"),
    tools=[YFinanceTools(
        stock_price=True,
        analyst_recommendations=True,
        stock_fundamentals=True
    )],
    show_tool_calls=True,
    markdown=True,
    instructions=["Use tables to display data"]
)
