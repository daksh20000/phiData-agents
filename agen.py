
from phi.agent import Agent
from phi.model.groq import Groq
from phi.model.google import Gemini
from dotenv import load_dotenv
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.crawl4ai_tools import Crawl4aiTools

load_dotenv()
financeAgent = Agent(
    model= Gemini(id="gemini-1.5-flash"),
    tools= [YFinanceTools(stock_price= True, analyst_recommendations=True, stock_fundamentals= True )],
    show_tool_calls=True,
    markdown=True,
    instructions= ["Use tables to display data"],
)

webAgent = Agent(
    model = Gemini(id="gemini-1.5-flash"),
    tools=[Crawl4aiTools(max_length=None)],
    markdown=True,
    show_tool_calls=True
)

agentTeam = Agent(
    team=[webAgent,financeAgent],
    show_tool_calls=True,
    markdown=True,
    instructions=["include sources, use tables to display data"]
)

agentTeam.print_response("help distinguishbetween Nvidia and AMD", stream=True)