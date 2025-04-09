import streamlit as st
import os
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.yfinance import YFinanceTools
from agno.tools.duckduckgo import DuckDuckGoTools
import groq
from dotenv import load_dotenv
import time

# Load environment variables first
load_dotenv()

# Check if API key exists and set it manually if needed
if not os.getenv("GROQ_API_KEY"):
    st.error("GROQ_API_KEY not found in environment variables. Please add it to your .env file.")
    st.stop()

# Set API key explicitly
groq.api_key = os.getenv("GROQ_API_KEY")

# Import agent modules after setting API key
from agents.finance_agent import FinanceAgent

# Initialize only the finance agent first
finance_agent = FinanceAgent()

# Streamlit app title
st.title("Finance Agent App")

# User input for stock ticker
ticker_symbol = st.text_input("Enter Stock Ticker Symbol (e.g., TSLA):", "TSLA")

if st.button("Get Financial Insights"):
    if ticker_symbol:
        try:
            # First display a comprehensive report
            with st.spinner(f"Generating comprehensive financial report for {ticker_symbol}..."):
                st.subheader(f"📊 Comprehensive Financial Report for {ticker_symbol}")
                comprehensive_report = finance_agent.generate_comprehensive_report(ticker_symbol)
                st.markdown(comprehensive_report.content)
                
            # Then show historical price chart
            with st.spinner(f"Retrieving historical price data for {ticker_symbol}..."):
                st.subheader(f"📈 Historical Stock Price Data for {ticker_symbol}")
                historical_data = finance_agent.get_historical_price_data(ticker_symbol)
                st.line_chart(historical_data['Close'])
                
            # Add a divider
            st.markdown("---")
            
            # Include expand sections for detailed information
            with st.expander(f"Detailed Stock Fundamentals for {ticker_symbol}"):
                fundamentals_response = finance_agent.get_stock_fundamentals(ticker_symbol)
                st.markdown(fundamentals_response.content)
                
            with st.expander(f"Analyst Recommendations for {ticker_symbol}"):
                analyst_response = finance_agent.get_analyst_recommendations_and_news(ticker_symbol)
                st.markdown(analyst_response.content)
                
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
            st.info("Try again or use a different ticker symbol")
    else:
        st.error("Please enter a valid stock ticker symbol.")