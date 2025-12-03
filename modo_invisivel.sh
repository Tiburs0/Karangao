#!/bin/bash
# Script para executar o Chrome em display virtual (invisível)

echo "╔══════════════════════════════════════════════════════════════════════╗"
echo "║    Download de Boletos - Modo Invisível (Display Virtual)           ║"
echo "╚══════════════════════════════════════════════════════════════════════╝"
echo ""
echo "Este modo executa o Chrome completamente invisível usando Xvfb"
echo ""

# Verifica se xvfb está instalado
if ! command -v Xvfb &> /dev/null; then
    echo "❌ Xvfb não está instalado!"
    echo ""
    echo "Para instalar:"
    echo "  sudo apt-get install xvfb"
    echo ""
    exit 1
fi

echo "✓ Xvfb encontrado"
echo ""
echo "Iniciando display virtual..."

# Inicia Xvfb em display :99
Xvfb :99 -screen 0 1920x1080x24 &
XVFB_PID=$!

export DISPLAY=:99

echo "✓ Display virtual iniciado (PID: $XVFB_PID)"
echo ""
echo "Abrindo Chrome em modo debug (invisível)..."

google-chrome --remote-debugging-port=9222 --user-data-dir="/tmp/chrome_debug_invisible" --display=:99 &
CHROME_PID=$!

echo "✓ Chrome aberto (PID: $CHROME_PID)"
echo ""
echo "════════════════════════════════════════════════════════════════════════"
echo ""
echo "IMPORTANTE:"
echo "  - O Chrome está rodando INVISÍVEL no display virtual"
echo "  - Você NÃO verá a janela do navegador"
echo "  - Para ver o navegador, use VNC ou x11vnc"
echo ""
echo "Para usar:"
echo "  1. Acesse: http://localhost:9222"
echo "  2. Clique na aba do Bradesco"
echo "  3. Faça login manualmente através do DevTools"
echo "  4. Execute: python download_boletos_bradesco.py"
echo ""
echo "Para parar:"
echo "  kill $CHROME_PID"
echo "  kill $XVFB_PID"
echo ""
echo "════════════════════════════════════════════════════════════════════════"
echo ""
echo "Pressione CTRL+C para parar"

wait
