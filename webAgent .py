from phi.agent import Agent
from phi.tools.website import WebsiteTools
from phi.model .groq import Groq
from dotenv import load_dotenv
 
load_dotenv()

webAgent = Agent(
    model=Groq(id="deepseek-r1-distill-llama-70b"),
    tools=[WebsiteTools()],
     show_tool_calls=True,
     markdown=True,
     instructions=["scrape the data from the website"]
    )

webAgent.print_response("Search web page: 'https://github.com/daksh20000'")