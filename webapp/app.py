import streamlit as st
import pandas as pd
import joblib
import os

# =============================
# Configuración página
# =============================
st.set_page_config(
    page_title="S&P 500 Prediction App",
    page_icon="📈",
    layout="centered"
)

st.title("📈 S&P 500 Prediction App")
st.write(
    "Simula un escenario de mercado y obtén la probabilidad estimada "
    "de subida para el próximo período."
)

st.divider()

st.sidebar.header("⚙️ Configuración")

selected_model = st.sidebar.selectbox(
    "Selecciona el modelo",
    ["XGBoost", "Random Forest"]
)

# =============================
# Rutas seguras
# =============================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODELS_PATH = os.path.abspath(
    os.path.join(BASE_DIR, "..", "models")
)

model = joblib.load(
    os.path.join(MODELS_PATH, "xgboost-model-final.pkl")
)

# =============================
# Cargar modelo y scaler
# =============================

scaler = joblib.load(os.path.join(MODELS_PATH, "scaler.pkl"))
model = joblib.load(os.path.join(MODELS_PATH, "xgboost-model-final.pkl"))


@st.cache_resource
def load_model():
    return joblib.load(os.path.join(MODELS_PATH, "xgboost-model-final.pkl"))

@st.cache_resource
def load_scaler():
    return joblib.load(os.path.join(MODELS_PATH, "scaler.pkl"))

@st.cache_resource
def load_pipeline(model_name):

    if model_name == "XGBoost":
        return joblib.load(os.path.join(MODELS_PATH, "xgb_pipeline.pkl"))

    elif model_name == "Random Forest":
        return joblib.load(os.path.join(MODELS_PATH, "rf_pipeline.pkl"))

pipeline = load_pipeline(selected_model)


# =============================
# Inputs del usuario
# =============================
st.subheader("🔧 Introduce las variables del mercado")

col1, col2 = st.columns(2)

with col1:
    price_change_5d = st.number_input(
        "📈 Cambio precio 5 días (%)",
        min_value=-50.0,
        max_value=50.0,
        value=0.0,
        step=0.1
    ) / 100

    price_vs_sma20 = st.slider(
        "📊 Precio vs SMA20 (%)",
        min_value=-20.0,
        max_value=20.0,
        value=0.0,
        step=0.1
    ) / 100

    volume_ratio = st.slider(
        "🔊 Volumen relativo",
        min_value=0.0,
        max_value=5.0,
        value=1.0,
        step=0.1
    )

with col2:
    rsi_label = st.selectbox(
        "🚀 Fuerza RSI",
        ["Débil (<40)", "Neutral (40-60)", "Fuerte (>60)"]
    )

    vol_level_label = st.selectbox(
        "⚡ Nivel de volatilidad",
        ["Baja", "Media", "Alta"]
    )

# =============================
# Mapas categóricos
# =============================
rsi_map = {
    "Débil (<40)": 0,
    "Neutral (40-60)": 1,
    "Fuerte (>60)": 2
}

vol_map = {
    "Baja": 0,
    "Media": 1,
    "Alta": 2
}

# =============================
# Botón predicción
# =============================
if st.button("🔍 Evaluar escenario"):

    # Crear DataFrame con mismo orden de entrenamiento
    X = pd.DataFrame([{
        "Price_Change_5d": price_change_5d,
        "price_vs_sma20": price_vs_sma20,
        "rsi_strength": rsi_map[rsi_label],
        "Volume_Ratio": volume_ratio,
        "vol_level": vol_map[vol_level_label]
    }])

    feature_order = [
        "Price_Change_5d",
        "price_vs_sma20",
        "rsi_strength",
        "Volume_Ratio",
        "vol_level"
    ]

    X = X[feature_order]

    # 🔥 Escalar TODO (porque así entrenaste)
    X_scaled = pd.DataFrame(
        scaler.transform(X),
        columns=X.columns
    )

    # Predicción
    prob_up = model.predict_proba(X_scaled)[0, 1]
    prob_down = model.predict_proba(X_scaled)[0, 0]

    st.divider()
    st.subheader("📊 Resultado")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Probabilidad subida", f"{prob_up*100:.1f}%")

    with col2:
        st.metric("Probabilidad bajada", f"{prob_down*100:.1f}%")

    if prob_up > 0.65:
        st.success("🟢 Señal fuerte alcista")
    elif prob_up > 0.5:
        st.warning("🟡 Señal moderada")
    else:
        st.error("🔴 Baja probabilidad de subida")

    st.caption("⚠️ Esta herramienta es informativa y no constituye asesoramiento financiero.")
