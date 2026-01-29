import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
import plotly.graph_objects as go
from datetime import timedelta

# 1. Configuración de la página
st.set_page_config(page_title="QuantVision IA", page_icon="📈", layout="wide")

# 2. Encabezado
st.title("📈 QuantVision IA: Market Forecasting Engine")
st.markdown("Análisis predictivo con **Random Forest**. Proyección limpia a 15 días.")

# 3. Barra Lateral
st.sidebar.header("⚙️ Configuración Visual")
ticker = st.sidebar.text_input("Activo (ej. BTC-USD, NVDA)", value="NVDA").upper()
meses_vista = st.sidebar.slider("Meses visibles", 6, 48, 12)

# Parámetros fijos
MESES_ENTRENAMIENTO = 48
ARBOLES_IA = 500

if st.sidebar.button("🚀 Ejecutar Análisis"):
    with st.spinner(f'Procesando {ticker}...'):
        data = yf.download(ticker, period=f"{MESES_ENTRENAMIENTO}mo", interval="1d")
        
        if data.empty:
            st.error("No se encontraron datos.")
        else:
            # Procesamiento de datos
            df = pd.DataFrame(data['Close']).copy()
            df.columns = ['Close']
            df['S_10'] = df['Close'].rolling(window=10).mean()
            df['S_30'] = df['Close'].rolling(window=30).mean()
            df['Mom'] = df['Close'].pct_change()
            df = df.dropna()

            # Entrenamiento IA
            X = df[['S_10', 'S_30', 'Mom']]
            y = df['Close']
            model = RandomForestRegressor(n_estimators=ARBOLES_IA, random_state=42)
            model.fit(X.values, y.values.ravel())

            # Predicción recursiva
            futuro_precios = []
            fechas_futuras = []
            ultima_fecha = df.index[-1]
            precio_actual = float(df['Close'].iloc[-1])
            temp_df = df.copy()

            for i in range(1, 16):
                s10 = temp_df['Close'].rolling(window=10).mean().iloc[-1]
                s30 = temp_df['Close'].rolling(window=30).mean().iloc[-1]
                mom = temp_df['Close'].pct_change().iloc[-1]
                pred = model.predict([[s10, s30, mom]])[0]
                
                futuro_precios.append(pred)
                nueva_fecha = ultima_fecha + timedelta(days=i)
                fechas_futuras.append(nueva_fecha)
                
                nueva_fila = pd.DataFrame({'Close': [pred]}, index=[nueva_fecha])
                temp_df = pd.concat([temp_df, nueva_fila])

            # Métricas
            st.markdown("---")
            precio_15d = futuro_precios[-1]
            rendimiento = ((precio_15d / precio_actual) - 1) * 100
            tendencia = "ALCISTA 🟢" if rendimiento > 0 else "BAJISTA 🔴"

            c1, c2, c3 = st.columns(3)
            c1.metric("Precio Actual", f"${precio_actual:,.2f}")
            c2.metric("Predicción 15d", f"${precio_15d:,.2f}", f"{rendimiento:.2f}%")
            c3.metric("Tendencia", tendencia)

            # --- GRÁFICA INTERACTIVA PULIDA ---
            puntos_vista = meses_vista * 21
            hist_df = df.tail(puntos_vista)

            fig = go.Figure()

            # 1. Histórico Real
            fig.add_trace(go.Scatter(
                x=hist_df.index, y=hist_df['Close'].values.flatten(),
                mode='lines', name='Histórico Real',
                line=dict(color='#00d4ff', width=2),
                hovertemplate="Fecha: %{x}<br>Precio: %{y:,.2f}<extra>REAL</extra>"
            ))

            # 2. Proyección IA
            fechas_proyeccion = [df.index[-1]] + fechas_futuras
            precios_proyeccion = [precio_actual] + futuro_precios
            
            fig.add_trace(go.Scatter(
                x=fechas_proyeccion, y=precios_proyeccion,
                mode='lines+markers', name='Proyección IA',
                line=dict(color='#ff4b4b', width=2, dash='dash'),
                marker=dict(size=4),
                hovertemplate="Fecha: %{x}<br>Predicción: %{y:,.2f}<extra>IA</extra>"
            ))

            # 3. Rango de Incertidumbre ATENUADO (Ajuste de precisión)
            volatilidad_base = df['Mom'].std()
            # Reducimos el impacto para que el rango sea discreto y profesional
            factor_ajuste = 0.5 
            upper_bound = [p + (precio_actual * volatilidad_base * factor_ajuste * np.sqrt(i)) for i, p in enumerate(precios_proyeccion)]
            lower_bound = [p - (precio_actual * volatilidad_base * factor_ajuste * np.sqrt(i)) for i, p in enumerate(precios_proyeccion)]

            fig.add_trace(go.Scatter(
                x=fechas_proyeccion + fechas_proyeccion[::-1],
                y=upper_bound + lower_bound[::-1],
                fill='toself',
                fillcolor='rgba(255, 75, 75, 0.1)', # Sombreado muy suave
                line=dict(color='rgba(255,255,255,0)'),
                hoverinfo="skip",
                name='Zona de Probabilidad'
            ))

            fig.update_layout(
                template="plotly_dark",
                hovermode="x unified",
                xaxis=dict(range=[hist_df.index[0], fechas_futuras[-1]], showgrid=False),
                yaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.05)'),
                legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
            )

            st.plotly_chart(fig, use_container_width=True)

else:
    st.info("👋 Selecciona un activo y ajusta el zoom de la gráfica.")