# 📈 AI Asset Investment Simulator

Un simulador de inversiones avanzado que combina análisis cuantitativo tradicional con **Inteligencia Artificial** para la predicción de activos financieros en tiempo real.

Este proyecto permite analizar cualquier ticker de Yahoo Finance (Acciones, Criptomonedas, ETFs), entrenar un modelo de Machine Learning y proyectar tendencias futuras con márgenes de probabilidad.



## 🧠 Documentación del Proyecto (Notion)
Puedes ver el desglose detallado de la lógica, los objetivos de negocio y el proceso de desarrollo en mi documentación técnica:
👉 **[Ver Documentación en Notion](https://www.notion.so/AI-Asset-Investment-Simulator-2f7227a9f96d80148631fcd65e328b6d)**

## ✨ Características Principales

* **IA con Random Forest:** Utiliza un modelo de ensamble de 200 árboles de decisión para proyectar los precios de los próximos 15 días.
* **Análisis Dinámico:** Capacidad de procesar cualquier activo (ej. `BTC-USD`, `NVDA`, `AAPL`) con datos actualizados al momento de la ejecución.
* **Feature Engineering:** El modelo no solo mira el precio, sino que interpreta indicadores clave:
    * **Momentum:** Velocidad de los cambios de precio.
    * **Volatilidad:** Desviación estándar para medir el riesgo.
    * **Medias Móviles (MA10/MA30):** Tendencias de corto y mediano plazo.
* **Visualización Pro:** Gráficas con **Bandas de Confianza** que muestran el rango de incertidumbre estadística de la predicción.



## 🛠️ Stack Tecnológico

* **Lenguaje:** Python 3.x
* **Data:** `yfinance` (Yahoo Finance API)
* **Análisis de Datos:** `pandas` & `numpy`
* **Machine Learning:** `scikit-learn` (Random Forest Regressor)
* **Visualización:** `matplotlib`

## 📦 Instalación y Uso

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/sklnrv/ai-asset-investment-simulator.git](https://github.com/sklnrv/ai-asset-investment-simulator.git)
   cd ai-asset-investment-simulator
Instalar dependencias: Se recomienda usar un entorno virtual (venv).

Bash

python -m pip install -r requirements.txt

Ejecutar el simulador:

Bash

python AIsimulator.py

## 📊 Cómo interpretar los resultados
Línea Azul: Precio real histórico de los últimos 6 meses.

Línea Roja Punteada: Proyección de la IA para los próximos 15 días.

Sombreado Rojo (Alpha): Rango de Probabilidad. Debido a la volatilidad, la IA estima que el precio se mantendrá dentro de esta zona con mayor probabilidad.

## Descargo de responsabilidad
Este proyecto tiene fines educativos y de portafolio técnico. No constituye asesoramiento financiero real.
