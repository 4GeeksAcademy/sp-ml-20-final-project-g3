# 📈 Predicción de Retorno a 10 Días

Este proyecto consiste en desarrollar un modelo de machine learning para predecir si una acción del índice S&P 500 aumentará su precio en al menos un 1% durante los próximos 10 días hábiles. Para ello, se utilizan datos históricos y variables técnicas de mercado con el fin de identificar patrones que anticipen movimientos positivos en el corto plazo.

Se probaron múltiples modelos de machine learning, entre ellos XGBoost y Random Forest, que son los dos seleccionados como finales para su optimización y despliegue en una aplicación web mediante Streamlit. Esta aplicación permite al usuario elegir entre ambos modelos para hacer predicciones en tiempo real.

---

## 👥 Créditos

**Colaboradores:**  
- Josefina Aispuro Merelles  
- Saray Ruiz Ruiz  
- Guillermo Rafael Lugo Ramos  

---

## 🎯 Objetivo del Proyecto

Crear un modelo de clasificación binaria que indique si una acción tendrá un retorno positivo mayor o igual al 1% en los siguientes 10 días, basándose en indicadores técnicos, volumen, volatilidad y datos históricos ajustados.

---

## 📊 Descripción de los Datos

Los datos utilizados provienen del dataset "Advanced Stock Dataset" disponible en Kaggle, construido con información histórica del Yahoo Finance API para las empresas del S&P 500 en aproximadamente los últimos cinco años.

El dataset contiene más de 620,000 registros diarios y 73 características, incluyendo precios ajustados, indicadores técnicos como medias móviles, RSI, MACD, volatilidad, y variables rezagadas para capturar la dinámica temporal. La variable objetivo es binaria y representa si el retorno acumulado en los próximos 10 días supera el 1%.

---

## 🗂 Estructura del Proyecto

```
SP-ML-20-FINAL-PROJECT-G3/
├── 📁 .vscode/           # Configuraciones de VSCode  
├── 📁 data/  
│   ├── 📁 processed/     # Datos procesados y listos para modelar  
│   └── 📁 raw/           # Datos originales sin procesar  
├── 📁 notebooks/  
│   ├── 📁 EDAs-1/        # Análisis exploratorio objetivo principal  
│   ├── 📁 EDAs-2/        # Análisis inicial para segundo objetivo (no finalizado)  
│   ├── 📁 final-models/  # Modelos finales optimizados (Gradient Boosting y Random Forest)  
│   └── 📁 test-models/   # Modelos probados durante experimentación  
├── 📁 webapp/            # Código fuente de la app Streamlit  
├── .gitignore            # Archivo para ignorar archivos en Git  
├── README_ES.md          # Documentación en español  
├── README_EN.md          # Documentación en inglés  
└── requirements.txt      # Dependencias del proyecto  
```

---

## 🛠 Tecnologías y Herramientas

- Python 3.10.11
- `numpy`, `pandas`, `scikit-learn`, `xgboost`, `randomforest`, `streamlit`, entre otras librerías.  
- Jupyter Notebooks para análisis y experimentación.  
- Streamlit para despliegue web interactivo.

---

## 🚀 Metodología

1. **Exploración y Análisis de Datos:**  
   Análisis exhaustivo de las características y variables del dataset para comprender su comportamiento.

2. **Preprocesamiento y Feature Engineering:**  
   Limpieza, creación de variables técnicas y rezagadas que capturan patrones temporales.

3. **Entrenamiento y Optimización de Modelos:**  
   Se entrenaron varios modelos supervisados, seleccionando XGBoost y Random Forest como los más efectivos.

4. **Evaluación de Resultados:**  
   Validación mediante métricas de clasificación y análisis comparativo entre modelos.

5. **Despliegue:**  
   Desarrollo de una aplicación web en Streamlit que permite seleccionar modelo y predecir retornos.

---

## 🌐 Aplicación Web

Para ejecutar la aplicación localmente, usar el siguiente comando desde la raíz del proyecto:

streamlit run webapp/app.py

---


## 📋 Instalación y Uso

Clonar el repositorio:
```
git clone <https://github.com/4GeeksAcademy/sp-ml-20-final-project-g3>
```

Instalar dependencias:
```
pip install -r requirements.txt
```

Ejecutar la aplicación Streamlit:
```
streamlit run webapp/app.py
```

---


## 🤝 Agradecimientos

Gracias a 4Geeks Academy por la formación y a nuestros mentores por su apoyo durante el desarrollo del proyecto.
