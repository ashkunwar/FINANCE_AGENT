from transformers import pipeline
from rapidfuzz.fuzz import partial_ratio
import yfinance as yf
import pandas as pd

def analyze_headline_sentiment(headlines):
    sentiment_pipeline = pipeline("sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment-latest")
    results = []
    for headline in headlines:
        sentiment = sentiment_pipeline(headline)[0]
        results.append({
            "headline": headline,
            "sentiment": sentiment['label'],
            "score": sentiment['score']
        })
    return pd.DataFrame(results)

def filter_news_by_sentiment(ticker_symbol, news_items, fuzzy_threshold=60):
    ticker = yf.Ticker(ticker_symbol)
    company_name = ticker.info.get('longName', ticker_symbol)
    
    def extract_text(item):
        content = item.get('content', '')
        if isinstance(content, dict):
            return content.get('title', str(content))
        elif isinstance(content, str):
            return content
        else:
            return str(content)

    filtered_news = []
    for item in news_items:
        text = extract_text(item)
        text_lower = text.lower()
        ticker_present = ticker_symbol.lower() in text_lower
        similarity = partial_ratio(company_name.lower(), text_lower)
        if ticker_present or similarity >= fuzzy_threshold:
            filtered_news.append(text)

    if len(filtered_news) < 5:
        for item in news_items:
            text = extract_text(item)
            if text not in filtered_news:
                filtered_news.append(text)
            if len(filtered_news) >= 5:
                break

    return filtered_news[:7]  # Return top 7 headlines