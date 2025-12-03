@echo off
REM Script para executar o download de boletos no Windows
REM Criado para facilitar a execucao duplo-clique

echo ===============================================
echo   Download de Boletos Bradesco - Windows
echo ===============================================
echo.

REM Verifica se Python esta instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERRO] Python nao encontrado!
    echo.
    echo Por favor, instale Python 3.8+ de https://www.python.org/downloads/
    echo.
    pause
    exit /b 1
)

echo [INFO] Python encontrado!
echo.

REM Verifica se as dependencias estao instaladas
echo [INFO] Verificando dependencias...
pip show selenium >nul 2>&1
if errorlevel 1 (
    echo [AVISO] Dependencias nao encontradas!
    echo [INFO] Instalando dependencias...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo [ERRO] Falha ao instalar dependencias!
        pause
        exit /b 1
    )
)

echo [INFO] Dependencias OK!
echo.
echo ===============================================
echo   Iniciando script...
echo ===============================================
echo.

REM Executa o script principal
python download_boletos_bradesco.py

echo.
echo ===============================================
echo   Script finalizado!
echo ===============================================
echo.
pause
