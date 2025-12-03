#!/bin/bash
# Script auxiliar para usar o download de boletos

echo "╔══════════════════════════════════════════════════════════════════════╗"
echo "║        Download Automático de Boletos - Bradesco                     ║"
echo "╚══════════════════════════════════════════════════════════════════════╝"
echo ""
echo "📋 PASSO A PASSO:"
echo ""
echo "1️⃣  Feche todas as janelas do Chrome"
echo ""
echo "2️⃣  Execute o comando abaixo para abrir o Chrome em modo debug:"
echo ""
echo "    google-chrome --remote-debugging-port=9222 --user-data-dir=\"/tmp/chrome_debug\""
echo ""
echo "3️⃣  No Chrome que abriu:"
echo "    - Acesse o site do Bradesco"
echo "    - Faça login"
echo "    - Navegue até a página de boletos"
echo ""
echo "4️⃣  Execute o script Python:"
echo ""
echo "    python download_boletos_bradesco.py"
echo ""
echo "    OU"
echo ""
echo "    python exemplo_uso_chrome_debug.py"
echo ""
echo "══════════════════════════════════════════════════════════════════════"
echo ""
echo "Deseja abrir o Chrome em modo debug agora? (s/N)"
read -r resposta

if [[ "$resposta" =~ ^[Ss]$ ]]; then
    echo ""
    echo "✓ Abrindo Chrome em modo debug..."
    google-chrome --remote-debugging-port=9222 --user-data-dir="/tmp/chrome_debug" &
    sleep 2
    echo ""
    echo "✓ Chrome aberto! Faça login no Bradesco e vá até a página de boletos."
    echo "✓ Depois execute: python download_boletos_bradesco.py"
else
    echo ""
    echo "OK. Execute os passos manualmente quando estiver pronto."
fi
