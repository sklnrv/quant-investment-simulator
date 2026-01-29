@echo off
title Lanzador AI Asset Investment Simulator
echo ======================================================
echo    Iniciando AI Asset Investment Simulator...
echo ======================================================

:: 1. Crear entorno virtual si no existe
if not exist "env_simulator" (
    echo [1/3] Creando entorno virtual de Python...
    python -m venv env_simulator
)

:: 2. Activar e instalar dependencias
echo [2/3] Verificando y actualizando librerias...
call env_simulator\Scripts\activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

:: 3. Ejecutar Streamlit usando el modulo de Python del entorno
echo [3/3] Lanzando Dashboard interactivo...
echo.
:: Usamos "python -m streamlit" para asegurar que use el del entorno virtual
python -m streamlit run app.py

:: Si hay un error, el 'pause' evitara que la ventana se cierre sola
if %errorlevel% neq 0 (
    echo.
    echo ------------------------------------------------------
    echo ERROR: Hubo un problema al iniciar el simulador.
    pause
)