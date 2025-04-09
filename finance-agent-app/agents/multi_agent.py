from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.yfinance import YFinanceTools
from agno.tools.duckduckgo import DuckDuckGoTools
import os
import groq
import pandas as pd
import matplotlib.pyplot as plt
from textblob import TextBlob
import yfinance as yf
from dotenv import load_dotenv

load_dotenv()
groq.api_key = os.getenv("GROQ_API_KEY")

class MultiAgent:
    def __init__(self, finance_agent, web_search_agent):
        self.finance_agent = finance_agent
        self.web_search_agent = web_search_agent
        self.multi_ai_agent = Agent(
            team=[web_search_agent.agent, finance_agent.agent],
            model=Groq(id="qwen-2.5-32b"),
            instructions=[
                "Always include sources",
                "Use tables to display data",
                "Aggregate results from multiple tools"
            ],
            show_tool_calls=True,
            markdown=True,
        )
    
    def get_analyst_recommendations_and_news(self, ticker_symbol):
        response = self.multi_ai_agent.print_response(
            f"Summarize analyst recommendations and share the latest news for {ticker_symbol}. " 
            f"Search for any recent significant developments about this company.",
            stream=False
        )
        return response
    
    def get_market_insights(self, query):
        response = self.multi_ai_agent.print_response(
            f"Provide comprehensive market insights on {query}, including both financial data and news analysis.", 
            stream=False
        )
        return response