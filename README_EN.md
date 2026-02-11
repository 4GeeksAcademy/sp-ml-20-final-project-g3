# 📈 S&P 500 10-Day Return Prediction

This project consists of developing a machine learning model to predict whether a stock in the S&P 500 index will increase its price by at least 1% over the next 10 trading days. Historical data and technical market indicators are used to identify patterns that anticipate short-term positive price movements.

Multiple machine learning models were tested, including Gradient and Random Forest, which were selected as the final models for optimization and deployment in a web application using Streamlit. This application allows the user to choose between both models to make real-time predictions.

---

## 👥 Credits

**Collaborators:**  
- Josefina Aispuro Merelles  
- Saray Ruiz Ruiz  
- Guillermo Rafael Lugo Ramos  

---

## 🎯 Project Goal

Create a binary classification model that indicates whether a stock will have a positive return greater than or equal to 1% in the next 10 days, based on technical indicators, volume, volatility, and adjusted historical data.

---

## 📊 Data Description

The data used comes from the "Advanced Stock Dataset" available on Kaggle, built with historical information from the Yahoo Finance API for S&P 500 companies over approximately the last five years.

The dataset contains over 620,000 daily records and 73 features, including adjusted prices, technical indicators such as moving averages, RSI, MACD, volatility, and lagged variables to capture temporal dynamics. The target variable is binary and represents whether the cumulative return over the next 10 days exceeds 1%.

---

## 🗂 Project Structure

```
SP-ML-20-FINAL-PROJECT-G3/
├── 📁 .vscode/           # VSCode configurations
├── 📁 data/  
│   ├── 📁 processed/     # Processed data ready for modeling
│   └── 📁 raw/           # Original raw data
├── 📁 notebooks/  
│   ├── 📁 EDAs-1/        # Exploratory analysis for main objective
│   ├── 📁 EDAs-2/        # Initial analysis for second objective (not finalized)
│   ├── 📁 final-models/  # Optimized final models (Gradient Boosting and Random Forest)
│   └── 📁 test-models/   # Models tested during experimentation
├── 📁 webapp/            # Streamlit app source code
├── .gitignore            # Git ignore file
├── README_ES.md          # Documentation in Spanish 
├── README_EN.md          # Documentation in English
└── requirements.txt      # Project dependencies
```

---

## 🛠 Technologies and Tools

- Python 3.10.11
- `numpy`, `pandas`, `scikit-learn`, `xgboost`, `randomforest`, `streamlit`, among other libraries.  
- Jupyter Notebooks for analysis and experimentation.  
- Streamlit for interactive web deployment.

---

## 🚀 Methodology

1. **Data Exploration and Analysis:**  
   Thorough analysis of dataset features and variables to understand their behavior.

2. **Preprocessing and Feature Engineering:**  
   Cleaning and creating technical and lagged variables to capture temporal patterns.

3. **Model Training and Optimization:**  
   Multiple supervised models were trained, selecting XGBoost and Random Forest as the most effective.

4. **Results Evaluation:**  
   Validation using classification metrics and comparative analysis between models.

5. **Deployment:**  
   Development of a Streamlit web application that allows users to select a model and predict returns.

---

## 🌐 Web Application

To run the application locally, use the following command from the project root:
```
cd webapp
streamlit run app.py
```

---


## 📊 Data Sources

The application sources S&P 500 index data from two reliable web pages, using only the indicators required for the prediction:

TradingView – https://es.tradingview.com/symbols/SPX/technicals/?exchange=SP

Yahoo Finance – https://es.finance.yahoo.com/quote/%5EGSPC/


---

## 📋 Installation and Usage

Clone the repository:
```
git clone <https://github.com/4GeeksAcademy/sp-ml-20-final-project-g3>
```

Install dependencies:
```
pip install -r requirements.txt
```

Run the Streamlit application:
```
cd webapp
streamlit run app.py
```

---

## 🤝 Acknowledgements

Thanks to 4Geeks Academy for the training and to our mentors for their support during the project development.

