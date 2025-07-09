# Multi-Agent AI System using PHI, Gemini, and Groq

This project implements a multi-agent architecture using the [PHI](https://github.com/typetheta/phi) framework, combining Google's Gemini models, Groq LLMs, and custom tools for structured financial data extraction and web scraping.

## Overview

The system is composed of the following agents:

- **Finance Agent**: Queries financial data including stock prices, fundamentals, and analyst recommendations using Gemini and YFinanceTools.
- **Web Agent**: Scrapes and summarizes web content using Crawl4aiTools or WebsiteTools, powered by either Gemini or Groq models.
- **Team Agent**: Coordinates multiple agents to handle complex queries that require information retrieval and structured presentation.

## Agents Configuration

### Finance Agent

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
