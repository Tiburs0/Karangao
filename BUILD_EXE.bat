@echo off
REM Script para criar executavel Windows (.exe)
REM Usa PyInstaller para empacotar o script Python

echo ===============================================
echo   Build Executavel - Download Boletos
echo ===============================================
echo.

REM Verifica se PyInstaller esta instalado
pip show pyinstaller >nul 2>&1
if errorlevel 1 (
    echo [INFO] PyInstaller nao encontrado. Instalando...
    pip install pyinstaller
    if errorlevel 1 (
        echo [ERRO] Falha ao instalar PyInstaller!
        pause
        exit /b 1
    )
)

echo [INFO] PyInstaller OK!
echo.

REM Remove builds anteriores
if exist "build" (
    echo [INFO] Removendo build anterior...
    rmdir /s /q build
)
if exist "dist" (
    echo [INFO] Removendo dist anterior...
    rmdir /s /q dist
)
if exist "*.spec" (
    echo [INFO] Removendo spec anterior...
    del /q *.spec
)

echo.
echo [INFO] Criando executavel...
echo.

REM Cria o executavel
REM Opcoes:
REM   --onefile         = Cria um unico arquivo .exe
REM   --windowed        = Nao mostra console (apenas GUI)
REM   --noconsole       = Alternativa para --windowed
REM   --icon=icone.ico  = Define icone (se existir)
REM   --name            = Nome do executavel
REM   --clean           = Limpa cache antes de buildar

pyinstaller ^
    --onefile ^
    --name="DownloadBoletos" ^
    --clean ^
    download_boletos_bradesco.py

if errorlevel 1 (
    echo.
    echo [ERRO] Falha ao criar executavel!
    echo.
    pause
    exit /b 1
)

echo.
echo ===============================================
echo   Build Concluido!
echo ===============================================
echo.
echo O executavel esta em: dist\DownloadBoletos.exe
echo.
echo IMPORTANTE:
echo - Tamanho aproximado: 30-50 MB
echo - Primeira execucao pode ser lenta
echo - Antivirus pode detectar como suspeito (falso positivo)
echo.

REM Verifica se o executavel foi criado
if exist "dist\DownloadBoletos.exe" (
    echo [INFO] Executavel criado com sucesso!
    echo [INFO] Tamanho:
    dir dist\DownloadBoletos.exe | find "DownloadBoletos.exe"
) else (
    echo [AVISO] Executavel nao encontrado em dist\
)

echo.
pause
