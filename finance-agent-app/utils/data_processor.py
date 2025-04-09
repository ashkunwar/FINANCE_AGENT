import pandas as pd
import os
from dotenv import load_dotenv  
load_dotenv()
import groq
groq.api_key = os.getenv("GROQ_API_KEY")
from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.yfinance import YFinanceTools
from agno.tools.duckduckgo import DuckDuckGoTools
from agents.finance_agent import FinanceAgent
from agents.web_search_agent import WebSearchAgent
from agents.multi_agent import MultiAgent
import matplotlib.pyplot as plt
from textblob import TextBlob
from agents.finance_agent import FinanceAgent   
def fetch_financial_data(ticker_symbol):
    import yfinance as yf
    ticker = yf.Ticker(ticker_symbol)
    return ticker

def clean_data(data):
    if isinstance(data, pd.DataFrame):
        return data.dropna()
    return data

def fetch_and_clean_news(ticker_symbol):
    ticker = fetch_financial_data(ticker_symbol)
    news_items = ticker.news
    cleaned_news = [item for item in news_items if item.get('content')]
    return cleaned_news

def extract_fundamentals(ticker_symbol):
    ticker = fetch_financial_data(ticker_symbol)
    fundamentals = {
        "longName": ticker.info.get('longName', ticker_symbol),
        "marketCap": ticker.info.get('marketCap'),
        "peRatio": ticker.info.get('forwardPE'),
        "dividendYield": ticker.info.get('dividendYield')
    }
    return clean_data(fundamentals)