# FINAL PROJECT - SP500

### Objective 1: Next-Day Return Prediction
- Goal: train a machine learning model to predict whether a stock will increase by more than 1% on the next trading day, using information from the previous 30 days of S&P 500 market data.
- Description: The model will leverage technical indicators, price action, volume dynamics, volatility measures, and lagged features to learn short-term market patterns that precede significant positive price movements. This task is framed as a binary classification problem, where the target variable indicates whether the next-day return exceeds the 1% threshold.
- Purpose: to evaluate the feasibility of short-term return prediction using historical market data while strictly avoiding look-ahead bias and preserving the temporal structure of financial time series.

### Objective 2: Market Crisis / Risk Detection
- Goal: train a model to detect early warning patterns that typically occur before major market downturns or periods of extreme volatility in the S&P 500.
- Description: this model focuses on identifying abnormal behavior in volatility, volume, and price dynamics that may signal increased market risk or the onset of a crisis. The task can be approached using anomaly detection or risk classification, learning what constitutes “normal” market behavior and flagging deviations from it.
- Purpose: To provide a risk-awareness layer that complements the return prediction model by highlighting unstable market conditions where predictive confidence and trading strategies should be adjusted.

### Data origin and description
The data for this project comes from Kaggle, specifically the Advanced Stock Dataset by baidalinadilzhan, which is built using historical data retrieved from the Yahoo Finance API and covers approximately the past five years of trading for companies in the S&P 500 index. The dataset is structured with daily adjusted prices that account for corporate actions such as dividends and stock splits, making it suitable for financial analysis and time-series modeling.
The full dataset includes over 620,000 daily observations with 73 engineered features, such as opening, high, low, and closing prices, trading volume, technical indicators (e.g., moving averages, RSI), volatility measures, and multiple lagged variables, providing a rich foundation for tasks like return prediction, directional classification, and risk detection using machine learning.
WEB this data set:
https://www.kaggle.com/datasets/baidalinadilzhan/advanced-stock-dataset?resource=download