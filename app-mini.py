import streamlit as st
import numpy as np
import pandas as pd
import joblib

# =========================
# Cargar modelo y scaler
# =========================
model = joblib.load("models\simple_model.pkl")
scaler = joblib.load("models\scaler.pkl")

# =========================
# Configuración página
# =========================
st.set_page_config(
    page_title="Stock Opportunity Analyzer",
    page_icon="📈",
    layout="centered"
)

st.title("📈 Stock Opportunity Analyzer")
st.write(
    "Esta herramienta evalúa si una acción presenta una **oportunidad potencial para el próximo día**, "
    "utilizando información sencilla y fácil de interpretar."
)

st.divider()

# =========================
# Inputs del usuario
# =========================
st.subheader("🔧 Introduce la información de la acción")

price_change_5d = st.slider(
    "📈 Rendimiento últimos 5 días (%)",
    min_value=-10.0,
    max_value=10.0,
    value=0.0,
    step=0.1
) / 100

price_vs_sma20 = st.slider(
    "📊 Precio respecto a su media (20 días) (%)",
    min_value=-10.0,
    max_value=10.0,
    value=0.0,
    step=0.1
) / 100

rsi_strength_label = st.selectbox(
    "🚀 Fuerza del movimiento",
    ["Débil", "Neutral", "Fuerte"]
)

volume_ratio = st.slider(
    "🔊 Volumen actual vs normal",
    min_value=0.0,
    max_value=5.0,
    value=1.0,
    step=0.1
)

vol_level_label = st.selectbox(
    "⚡ Nivel de volatilidad",
    ["Baja", "Media", "Alta"]
)

market_risk_label = st.selectbox(
    "🌍 Riesgo general del mercado",
    ["Bajo", "Medio", "Alto"]
)

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

    X = pd.DataFrame([{
        "Price_Change_5d": price_change_5d,
        "price_vs_sma20": price_vs_sma20,
        "rsi_strength": rsi_map[rsi_strength_label],
        "Volume_Ratio": volume_ratio,
        "vol_level": vol_map[vol_level_label],
        "market_risk": risk_map[market_risk_label]
    }])

    # Escalado columnas numéricas
    scale_cols = ["Price_Change_5d", "price_vs_sma20", "Volume_Ratio"]
    X[scale_cols] = scaler.transform(X[scale_cols])

    prob = model.predict_proba(X)[0, 1]

    st.divider()
    st.subheader("📊 Resultado")

    st.metric(
        label="Probabilidad estimada de oportunidad",
        value=f"{prob*100:.1f}%"
    )

    # Interpretación
    if market_risk_label == "Alto":
        st.error("🔴 Mercado adverso. No se recomienda operar.")
    elif prob > 0.6:
        st.success("🟢 Oportunidad interesante para el próximo día.")
    elif prob > 0.4:
        st.warning("🟡 Oportunidad moderada. Precaución recomendada.")
    else:
        st.error("🔴 No se recomienda operar.")

    st.caption(
        "⚠️ Esta herramienta es solo informativa y no constituye asesoramiento financiero."
    )
