# 📉 Project Overview

This project has evolved from a basic quantitative script into a **professional-grade AI forecasting dashboard**. It demonstrates the bridge between Data Science and FinTech, leveraging Machine Learning to decode market patterns, quantify volatility-based risk, and project asset trajectories while eliminating emotional bias from the decision-making process.

---

## 🛠️ Design Choices

### 1. Recursive Multi-step Forecasting
Unlike static "one-shot" models, this system implements a **Recursive Forecasting** logic. The model predicts $t+1$, updates the technical indicators (SMA, Momentum), and uses that synthetic data to predict $t+2$, repeating the process for a full 15-day window.

### 2. High-Performance Ensemble Learning
* **Model:** `Random Forest Regressor`
* **Hyperparameters:** 500 Decision Trees ($n\_estimators=500$)
* **Lookback Period:** 48 months of daily OHLCV data for robust pattern recognition.

### 3. Advanced Feature Engineering
The AI doesn't just "see" price; it interprets the market's "DNA" through:
* **Momentum ($P_t / P_{t-1} - 1$):** To capture acceleration.
* **SMA 10/30:** To identify trend crossovers and support/resistance levels.
* **Volatility ($\sigma$):** Used both for training and for the statistical derivation of the confidence bands.

### 4. Interactive Financial UX
Migration from static `Matplotlib` renders to a **Plotly-powered interactive engine**. This allows for:
* **Dynamic Scaling:** Automatic adjustment of the Y-axis.
* **Data Inspection:** Hover tooltips for precise price/date validation.
* **Statistical Bands:** Implementation of a "Volatility Cone" based on $\sigma \cdot \sqrt{t}$ for realistic risk assessment.

---

## ⚠️ Current Limitations

* **Quantitative-Only Input:** The model relies on endogenous price data. It currently lacks **Natural Language Processing (NLP)** to factor in exogenous shocks (e.g., Fed rate hikes, earnings calls).
* **Frictionless Environment:** Calculations do not yet account for exchange fees, slippage, or tax implications.
* **Long-Only Bias:** The simulation assumes a spot-buying strategy without considering short-selling or hedging through derivatives.

---

## 🚀 Future Direction

The roadmap for this system includes:
* **Sentiment Engine:** Integrating News APIs and Reddit/X (Twitter) scrapers to correlate social sentiment with price action.
* **Portfolio Management (MPT):** Implementing **Modern Portfolio Theory** to suggest optimal risk-parity allocations between multiple tickers.
* **Risk Diagnostics:** Adding automated calculation of **Sharpe Ratio**, **Maximum Drawdown (MDD)**, and **Beta** relative to the S&P 500.
* **Cloud Deployment:** Migrating the local Streamlit instance to a persistent **Streamlit Cloud** or **AWS EC2** environment.