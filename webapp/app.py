import streamlit as st
import pandas as pd
from pickle import load

# Cargar modelo y columnas (ya definidas)
model = load(open("models/xgb-model-eda4.pkl", "rb"))
model_features = [
    'Close', 'Volume', 'Ticker', 'EMA_12', 'MACD', 'MACD_Signal', 'RSI',
    'BB_Upper', 'BB_Lower', 'BB_Position', 'Volatility', 'Price_Change',
    'Volume_Ratio', 'Volume_lag_1', 'Volume_lag_2', 'Volume_lag_3',
    'Volume_lag_5', 'Volume_lag_10', 'RSI_lag_1', 'MACD_lag_1',
    'Volatility_lag_1', 'retorno_5d', 'volatilidad_10d', 'MACD_Bullish',
    'RSI_Trend_Up', 'BB_Breakout', 'High_Volume_Signal'
]

st.title("Predicción de subida de precio al día siguiente")
st.markdown("Sube un archivo CSV con las columnas necesarias para que el modelo prediga si el precio subirá al menos 1% mañana.")
st.divider()

st.subheader("Columnas necesarias para el modelo")
st.write(model_features)

uploaded_file = st.file_uploader("Sube tu CSV aquí", type=["csv"])

# Botón siempre visible
if st.button("Predecir"):
    if uploaded_file is None:
        st.error("Primero debes subir un archivo CSV para habilitar la predicción.")
    else:
        input_data = pd.read_csv(uploaded_file)
        missing_cols = [col for col in model_features if col not in input_data.columns]
        if missing_cols:
            st.error(f"Faltan columnas en el CSV: {missing_cols}")
        else:
            X_input = input_data[model_features]
            prediction = model.predict(X_input)
            st.write("Predicciones:")
            st.write(prediction)