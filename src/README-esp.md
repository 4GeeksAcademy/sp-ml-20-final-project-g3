# PROYECTO FINAL - SP500

### Objetivo 1: Predicción del Retorno del Día Siguiente
- Objetivo: entrenar un modelo de machine learning para predecir si una acción aumentará más de un 1% en el siguiente día de trading, utilizando información de los últimos 30 días de datos del mercado del S&P 500.
- Descripción: el modelo aprovechará indicadores técnicos, acción del precio, dinámica del volumen, medidas de volatilidad y variables rezagadas para aprender patrones de mercado a corto plazo que preceden movimientos positivos significativos del precio. Esta tarea se plantea como un problema de clasificación binaria, donde la variable objetivo indica si el retorno del día siguiente supera el umbral del 1%.
- Propósito: evaluar la viabilidad de la predicción de retornos a corto plazo utilizando datos históricos de mercado, evitando estrictamente el look-ahead bias y preservando la estructura temporal de las series financieras.

### Objetivo 2: Detección de Crisis / Riesgo de Mercado
- Objetivo: entrenar un modelo para detectar patrones de alerta temprana que suelen ocurrir antes de caídas importantes del mercado o periodos de volatilidad extrema en el S&P 500.
- Descripción: este modelo se centra en identificar comportamientos anómalos en la volatilidad, el volumen y la dinámica del precio que puedan indicar un aumento del riesgo de mercado o el inicio de una crisis. La tarea puede abordarse mediante detección de anomalías o clasificación de riesgo, aprendiendo qué se considera un comportamiento “normal” del mercado y señalando desviaciones respecto a él.
- Propósito: proporcionar una capa de conciencia de riesgo que complemente el modelo de predicción de retornos, destacando condiciones de mercado inestables en las que la confianza predictiva y las estrategias de trading deberían ajustarse.

### Origen de los datos y descripción
Los datos de este proyecto provienen de Kaggle, del dataset Advanced Stock Dataset creado por baidalinadilzhan, que a su vez se basa en datos descargados de Yahoo Finance API, cubriendo aproximadamente los últimos cinco años de mercado para los componentes del índice S&P 500. Este conjunto de datos incluye observaciones diarias ajustadas por eventos corporativos como dividendos y splits, y está diseñado específicamente para análisis financiero y modelado de series temporales.
En total, el dataset contiene más de 600 000 registros diarios con 73 características que incluyen precios (Open, High, Low, Close), volumen, indicadores técnicos como medias móviles y RSI, métricas de volatilidad y múltiples variables con información histórica rezagada (lags), lo que lo hace adecuado para tareas de predicción de retornos, clasificación direccional y análisis de riesgo en machine learning financiero.
Enlace WEB del data set:
https://www.kaggle.com/datasets/baidalinadilzhan/advanced-stock-dataset?resource=download