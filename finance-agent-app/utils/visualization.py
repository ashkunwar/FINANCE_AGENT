def plot_historical_prices(hist_data, ticker_symbol):
    import matplotlib.pyplot as plt

    plt.figure(figsize=(10, 5))
    plt.plot(hist_data.index, hist_data['Close'], label=f"{ticker_symbol} Close Price", color="blue")
    plt.title(f"{ticker_symbol} Historical Closing Prices (Last 6 Months)")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_sentiment_analysis(sentiment_df):
    import matplotlib.pyplot as plt

    sentiment_counts = sentiment_df['sentiment'].value_counts()
    plt.figure(figsize=(8, 5))
    sentiment_counts.plot(kind='bar', color=['green', 'red', 'gray'])
    plt.title("Sentiment Analysis of News Headlines")
    plt.xlabel("Sentiment")
    plt.ylabel("Count")
    plt.xticks(rotation=0)
    plt.grid(axis='y')
    plt.tight_layout()
    plt.show()