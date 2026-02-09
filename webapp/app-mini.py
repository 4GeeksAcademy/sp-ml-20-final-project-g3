import streamlit as st
import numpy as np
import pandas as pd
import joblib
import os

# =========================
# Cargar modelo y scaler
# =========================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
modeds_path = os.path.abspath(
    os.path.join(BASE_DIR, "..", "models")
)
skaler_patch = os.path.abspath(
    os.path.join(BASE_DIR, "..", "models")
)


model = joblib.load(modeds_path)
model = joblib.load(skaler_path)
# =========================
# Configuración página
# =========================
st.set_page_config(page_title="Stock Opportunity Analyzer",
                   page_icon="📈",layout="centered")

st.title("📈 Stock Opportunity Analyzer")
st.write("Esta herramienta evalúa si una acción presenta una **oportunidad potencial para el próximo día**, "
    "utilizando información sencilla y fácil de interpretar.")

st.divider()

# =========================
# Inputs del usuario (Cajas de entrada)
# =========================
st.subheader("🔧 Introduce la información de la acción")

# Usamos columnas para que no ocupe tanto espacio vertical
col1, col2 = st.columns(2)

with col1:
    Price_Change_10d = st.number_input("📈 Cambio de precio 10 días (%)",
                                       value=0.0, 
                                       step=0.1) / 100
    
    price_vs_sma20 = st.number_input("📊 Precio respecto a su media (20 días) (%)",
                                     value=0.0, 
                                     step=0.1,
                                     format="%.2f") / 100

    rsi_strength_label = st.number_input("🚀 Fuerza del movimiento",
                                         value=0.0, 
                                         step=0.1,
                                         format="%.2f") / 100

with col2:
       volume_ratio = st.number_input("🔊 Volumen actual vs normal", 
                                      value=0.0, 
                                      step=0.1,
                                      format="%.2f") / 100

price_vs_sma20 = st.slider("📊 Precio respecto a su media (20 días) (%)",
                           min_value=-10.0,
                           max_value=10.0,
                           value=0.0,
                           step=0.1) / 100

volume_ratio = st.slider("🔊 Volumen actual vs normal",
                         min_value=0.0,
                         max_value=5.0,
                         value=1.0,
                         step=0.1)

vol_level_label = st.selectbox("⚡ Nivel de volatilidad",
                               ["Baja", "Media", "Alta"])

market_risk_label = st.selectbox("🌍 Riesgo general del mercado",
                                 ["Bajo", "Medio", "Alto"])

# =========================
# Mapeos categóricos
# =========================
rsi_map = {"Débil": 0, "Neutral": 1, "Fuerte": 2}
vol_map = {"Baja": 0, "Media": 1, "Alta": 2}
risk_map = {"Bajo": 0, "Medio": 1, "Alto": 2}

# =========================
# Botón de evaluación
# =========================
if st.button("🔍 Evaluar oportunidad"):

    X = pd.DataFrame([{"Price_Change_10d": Price_Change_10d,
                       "price_vs_sma20": price_vs_sma20,
                       "rsi_strength": rsi_map[rsi_strength_label],
                       "Volume_Ratio": volume_ratio,
                       "vol_level": vol_map[vol_level_label],
                       "market_risk": risk_map[market_risk_label]}])

    # Escalado columnas numéricas
    scale_cols = ["Price_Change_5d", "price_vs_sma20", "Volume_Ratio"]
    X[scale_cols] = scaler.transform(X[scale_cols])

    prob = model.predict_proba(X)[0, 1]

    st.divider()
    st.subheader("📊 Resultado")

    st.metric(label="Probabilidad estimada de oportunidad",
              value=f"{prob*100:.1f}%")

    # Interpretación
    if market_risk_label == "Alto":
        st.error("🔴 Mercado adverso. No se recomienda operar.")
    elif prob > 0.6:
        st.success("🟢 Oportunidad interesante para el próximo día.")
    elif prob > 0.4:
        st.warning("🟡 Oportunidad moderada. Precaución recomendada.")
    else:
        st.error("🔴 No se recomienda operar.")

    st.caption("⚠️ Esta herramienta es solo informativa y no constituye asesoramiento financiero.")
