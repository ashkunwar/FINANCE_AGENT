# Finance Agent App

## Overview
The Finance Agent App is a Streamlit application designed to provide users with insights into financial data, including stock fundamentals, analyst recommendations, and sentiment analysis of financial news. The app leverages various agents to fetch and process data, making it a comprehensive tool for financial analysis.

## Project Structure
```
finance-agent-app
├── app.py                  # Main entry point of the Streamlit application
├── agents                  # Contains agent implementations
│   ├── __init__.py        # Initializes the agents package
│   ├── finance_agent.py    # Implementation of the Finance AI Agent
│   ├── web_search_agent.py  # Implementation of the Web Search Agent
│   └── multi_agent.py      # Combines functionalities of finance and web search agents
├── utils                   # Contains utility functions
│   ├── __init__.py        # Initializes the utils package
│   ├── data_processor.py    # Functions for processing financial data
│   ├── visualization.py      # Functions for visualizing financial data
│   └── sentiment_analyzer.py # Functions for analyzing sentiment of news headlines
├── .env.example            # Template for environment variables
├── requirements.txt        # Lists necessary libraries and dependencies
└── README.md               # Documentation for the project
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd finance-agent-app
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required libraries:
   ```
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   - Copy `.env.example` to `.env` and fill in the necessary API keys and configurations.

## Usage

To run the Streamlit application, execute the following command:
```
streamlit run app.py
```

## Features
- Retrieve stock fundamentals and financial data.
- Get analyst recommendations and the latest news.
- Visualize historical stock prices.
- Analyze sentiment of news headlines related to stocks.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.