from pickle import load
import streamlit as st
import pandas as pd

# Cargar modelo
model = load(open("models/xgb_future_up_5d.pkl", "rb"))

st.title("Stock Movement Prediction (5D)")
st.markdown("Predicción de subida en los próximos 5 días")
st.divider()

st.write("Introduce los valores de las variables ya escaladas:")

# Ejemplo de inputs (ajusta a tus features reales)
rsi = st.number_input("RSI", value=0.0)
macd = st.number_input("MACD", value=0.0)
volatility = st.number_input("Volatility", value=0.0)
bb_position = st.number_input("BB Position", value=0.0)

if st.button("Predict"):
    X_input = pd.DataFrame([{
        "RSI": rsi,
        "MACD": macd,
        "Volatility": volatility,
        "BB_Position": bb_position
    }])

    prediction = model.predict(X_input)[0]
    proba = model.predict_proba(X_input)[0][1]

    st.divider()
    if prediction == 1:
        st.success(f"📈 Predicción: SUBE en 5 días (probabilidad {proba:.2%})")
    else:
        st.error(f"📉 Predicción: NO sube en 5 días (probabilidad {proba:.2%})")
    st.divider()