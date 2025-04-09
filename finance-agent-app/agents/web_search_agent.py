from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
import os
import groq
from dotenv import load_dotenv

load_dotenv()
groq.api_key = os.getenv("GROQ_API_KEY")

class WebSearchAgent:
    def __init__(self):
        self.agent = Agent(
            name="Web Search Agent",
            role="Search the web for financial news and information",
            model=Groq(id="qwen-2.5-32b"),
            tools=[DuckDuckGoTools()],
            instructions=["Always include sources"],
            markdown=True,
        )

    def search_financial_news(self, query):
        response = self.agent.print_response(
            f"Search for the latest financial news about {query}", 
            stream=False
        )
        return response
        
    def search_company_information(self, company_name):
        response = self.agent.print_response(
            f"Find detailed information about {company_name} company", 
            stream=False
        )
        return response