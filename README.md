# Finance Agent
![image](https://github.com/user-attachments/assets/840e1ca8-ea10-4e4b-bd4b-b4aeffd8924e)
Finance Agent is an interactive web application designed to generate comprehensive financial insights for stock ticker symbols. Built with [Streamlit](https://streamlit.io/), the application leverages tools such as [yfinance](https://pypi.org/project/yfinance/) to retrieve stock data, [Groq](https://groq.com/) for generating detailed reports, and additional modules for visualizing historical prices and stock fundamentals.

**Deployed at:** [https://huggingface.co/spaces/Ashkchamp/financeagent](https://huggingface.co/spaces/Ashkchamp/financeagent)

---

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

---

## Features

- **Comprehensive Financial Reports:** Generate detailed financial insights by providing a stock ticker.
- **Historical Price Visualization:** Display interactive charts showing historical price trends.
- **Detailed Fundamentals & Analyst Insights:** Review stock fundamentals and analyst recommendations in expandable sections.
- **Streamlit Powered Interface:** Benefit from an interactive web experience via Streamlit.
- **Modular Design:** Separates concerns with dedicated agents and tools (like yfinance and Groq) for maintainability.

---

## Prerequisites

- Python 3.7 or later
- API Key for [Groq](https://groq.com/) (set as environment variable `GROQ_API_KEY`)

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/ashkunwar/FINANCE_AGENT.git
cd FINANCE_AGENT
```

### 2. Create a Virtual Environment (Optional but Recommended)

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

If a `requirements.txt` file is present:

```bash
pip install -r requirements.txt
```

Otherwise, install manually:

```bash
pip install streamlit pandas yfinance matplotlib python-dotenv
```

> **Note:** Ensure that you have access to the custom modules (like `agno` and its submodules) if they're not available via PyPI.

---

## Configuration

### Environment Variables

Create a `.env` file in the project root and add your Groq API key:

```env
GROQ_API_KEY=your_groq_api_key_here
```

The app checks for this API key during startup and will display an error if it’s missing.

---

## Usage

### Run the Application

```bash
streamlit run app.py
```

### Interact with the App

- Enter a valid stock ticker symbol (e.g., `TSLA`).
- Click on the "Get Financial Insights" button.
- View the comprehensive financial report, historical price chart, detailed stock fundamentals, and analyst recommendations.

---

## Project Structure

```bash
FINANCE_AGENT/
├── app.py                      # Main Streamlit application entry point
├── agents/
│   └── finance_agent.py        # Contains the FinanceAgent class with report-generation logic
├── .env                        # Environment variables file (includes GROQ_API_KEY)
├── requirements.txt            # Project dependencies list
└── README.md                   # This README file
```

---

## Contributing

Contributions are welcome! If you wish to contribute by providing new features, reporting bugs, or suggesting improvements, please fork the repository and submit a pull request. Ensure your changes are well tested and documented.

---

## License

This project is licensed under the MIT License.

---

## Acknowledgements

- **Streamlit** for an intuitive web framework.
- **yfinance** for easy access to financial data.
- **Groq** for powering advanced financial insights.
- All contributors and community supporters.

