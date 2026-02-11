import streamlit as st
import pandas as pd
import joblib
import os


# Configuración página
st.set_page_config(page_title='S&P 500 Movement Predictor', page_icon='📈', layout='centered')

st.title('📈 S&P 500 Movement Predictor')
st.write('''Simula un escenario de mercado y obtén la probabilidad estimada de subida para el próximo período.''')

st.divider()


# Rutas
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODELS_PATH = os.path.abspath(os.path.join(BASE_DIR, '..', 'models'))


# Selector modelo
st.sidebar.header('⚙️ Configuración')

selected_model = st.sidebar.selectbox('Selecciona el modelo', ['Gradient Boosting (Optimista)', 'Random Forest (Conservador)'])

# Diccionario archivos
MODEL_FILES = {'Gradient Boosting (Optimista)': {'model': 'gradient-model-final.pkl', 'scaler': 'scaler-model-final.pkl'}, 
               'Random Forest (Conservador)': {'model': 'random-forest-model-final.pkl', 'scaler': 'scaler-model-final.pkl'}}


# Cargar modelo y scaler
@st.cache_resource
def load_model_and_scaler(model_name):

    files = MODEL_FILES[model_name]

    model = joblib.load(os.path.join(MODELS_PATH, files['model']))
    scaler = joblib.load(os.path.join(MODELS_PATH, files['scaler']))

    return model, scaler


model, scaler = load_model_and_scaler(selected_model)


# Inputs usuario
st.subheader('🔧 Introduce las variables del mercado')

col1, col2 = st.columns(2)

with col1:
    price_change_5d = st.number_input('📈 Cambio precio 5 días (%)', min_value=-50.0, max_value=50.0, value=0.0, step=0.1, format='%.3f', 
                                      help='''Representa cómo se ha comportado la acción durante los últimos 5 días. 
                                      Si subió usa el valor en positivo. Si bajó usa el valor en negativo''') / 100

    price_vs_sma20 = st.number_input('📊 Precio vs SMA20 (%)', min_value=-20.0, max_value=20.0, value=0.000, step=0.001, format='%.3f', 
                                     help='''Se calcula el precio de cierre entre la media movil simple 20 (SMA20) y al resultado se le resta 1. 
                                     Precio por encima → valor positivo. Precio por debajo → valor negativo.''') / 100

    volume_ratio = st.number_input('🔊 Volumen relativo', min_value=0.0, max_value=5.0, value=1.0, step=0.1, format='%.3f', 
                                   help='''Se calcula con el volumen actual divido entre el volumen promedio''')

with col2:
    rsi_label = st.selectbox('🚀 Fuerza RSI', ['Débil (<40)', 'Neutral (40-60)', 'Fuerte (>60)'], 
                             help='''Representa la intensidad del impulso reciente. En TradingView usar RSI: RSI < 40 → Débil. 
                             RSI 40–60 → Neutral. RSI > 60 → Fuerte.''')

    vol_level_label = st.selectbox('⚡ Nivel de volatilidad', ['Baja (<20)', 'Media (20-25)', 'Alta (>25)'], 
                                   help='''Para saber este indicador busca el simbolo VIX del S&P 500''')


# Mapas categóricos
rsi_map = {'Débil (<40)': 0, 'Neutral (40-60)': 1, 'Fuerte (>60)': 2}

vol_map = {'Baja (<20)': 0, 'Media (20-25)': 1, 'Alta (>25)': 2}


# Botón predicción
if st.button('🔍 Evaluar escenario'):

    X = pd.DataFrame([{'Price_Change_5d': price_change_5d, 'price_vs_sma20': price_vs_sma20, 
                       'rsi_strength': rsi_map[rsi_label], 'Volume_Ratio': volume_ratio, 'vol_level': vol_map[vol_level_label]}])


    # Forzar orden exacto del scaler
    feature_order = list(scaler.feature_names_in_)
    X = X[feature_order]

    X_scaled = scaler.transform(X)

    prob_up = model.predict_proba(X_scaled)[0, 1]
    prob_down = model.predict_proba(X_scaled)[0, 0]

    st.divider()
    st.subheader('📊 Resultado')

    col1, col2 = st.columns(2)

    with col1:
        st.metric(f'Probabilidad subida ({selected_model})', f'{prob_up*100:.1f}%')

    with col2:
        st.metric(f'Probabilidad bajada ({selected_model})', f'{prob_down*100:.1f}%')

    if prob_up > 0.65:
        st.success('🟢 Señal fuerte alcista')
    elif prob_up > 0.5:
        st.warning('🟡 Señal moderada')
    else:
        st.error('🔴 Baja probabilidad de subida')

    st.caption('⚠️ Esta herramienta es informativa y no constituye asesoramiento financiero.')
