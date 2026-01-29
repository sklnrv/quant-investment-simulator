# 📉 Project Overview

This project has evolved from a basic rule-based simulator into an **AI-powered financial forecasting tool**. It demonstrates the application of Machine Learning to analyze market trends, calculate risk volatility, and project asset prices while eliminating emotional bias from investment decisions.

## 🛠️ Design Choices
- **Machine Learning Integration:** Uses `Random Forest Regressor` to capture non-linear market patterns.
- **Feature Engineering:** Beyond price data, the system generates technical indicators (Momentum, Volatility, SMA) to feed the AI.
- **Real-Time Data:** Seamless integration with the Yahoo Finance API for up-to-the-minute market analysis.
- **Visual Confidence Intervals:** Implementation of probability bands to represent statistical uncertainty in predictions.

## ⚠️ Current Limitations
- **Simplified Trading:** Does not yet account for transaction fees or taxes.
- **Linear Derivation:** While Random Forest is robust, it does not factor in external macro-economic news (NLP/Sentiment analysis).
- **Execution:** Long-only strategy simulation.

## 🚀 Future Direction
The roadmap for this system includes:
- **Sentiment Analysis:** Integrating Natural Language Processing (NLP) to analyze financial news and social media.
- **Portfolio Optimization:** Implementing Modern Portfolio Theory (MPT) for 70/30 or risk-parity allocations.
- **Risk Metrics:** Adding Sharp Ratio, Max Drawdown, and Beta calculations.
- **Web Dashboard:** Deploying the tool as an interactive web app using Streamlit.