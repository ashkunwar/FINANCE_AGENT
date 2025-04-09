from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.yfinance import YFinanceTools
from agno.tools.duckduckgo import DuckDuckGoTools
import os
import groq
from dotenv import load_dotenv
import pandas as pd
import matplotlib.pyplot as plt
from textblob import TextBlob
import yfinance as yf

load_dotenv()
groq.api_key = os.getenv("GROQ_API_KEY")

class FinanceAgent:
    def __init__(self):
        self.agent = Agent(
            name="Finance AI Agent",
            model=Groq(id="qwen-2.5-32b"),
            tools=[
                YFinanceTools(
                    stock_price=True,
                    analyst_recommendations=True,
                    stock_fundamentals=True,
                    company_news=True
                ),
            ],
            instructions=["Use tables to display the data", "Always include sources"],
            show_tool_calls=True,
            markdown=True,
        )

    def get_analyst_recommendations_and_news(self, ticker_symbol):
        response = self.agent.run(
            f"Summarize analyst recommendations and share the latest news for {ticker_symbol}", stream=False
        )
        return response

    def get_stock_fundamentals(self, ticker_symbol):
        response = self.agent.run(
            f"Fetch stock fundamentals and key financial metrics for {ticker_symbol}", stream=False
        )
        return response

    def get_historical_price_data(self, ticker_symbol):
        company = yf.Ticker(ticker_symbol)
        hist_data = company.history(period="6mo")
        return hist_data

    def plot_historical_prices(self, hist_data, ticker_symbol):
        plt.figure(figsize=(10, 5))
        plt.plot(hist_data.index, hist_data['Close'], label=f"{ticker_symbol} Close Price", color="blue")
        plt.title(f"{ticker_symbol} Historical Closing Prices (Last 6 Months)")
        plt.xlabel("Date")
        plt.ylabel("Price (USD)")
        plt.legend()
        plt.grid(True)
        plt.show()
    # Add this method to the FinanceAgent class

  # Replace the generate_comprehensive_report method with this implementation

# Add this method to the FinanceAgent class

    def generate_comprehensive_report(self, ticker_symbol):
        prompt = f"""
        Generate a comprehensive financial report for {ticker_symbol} that includes:
        1. Company overview and recent performance
        2. Key financial metrics and stock fundamentals
        3. Detailed analyst recommendations with consensus rating
        4. Recent significant news and their impact on the stock
        5. Technical analysis of price trends
        6. Potential risks and opportunities

        Format as a professional report with clear sections.
        """
        response = self.agent.run(prompt, stream=False)
        return response