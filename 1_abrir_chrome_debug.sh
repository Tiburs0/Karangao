#!/bin/bash
# Passo 1: Abrir Chrome em modo debug

echo "╔══════════════════════════════════════════════════════════════════╗"
echo "║  PASSO 1: Abrindo Chrome para controle remoto                   ║"
echo "╚══════════════════════════════════════════════════════════════════╝"
echo ""
echo "✓ O Chrome vai abrir em modo especial"
echo "✓ Faça login no Bradesco normalmente"
echo "✓ Navegue até a página de BOLETOS"
echo ""
echo "⚠️  Depois execute: python download_simples.py"
echo ""
read -p "Pressione ENTER para abrir o Chrome... "

google-chrome --remote-debugging-port=9222 --user-data-dir="/tmp/chrome_debug" &

echo ""
echo "✅ Chrome aberto!"
echo "📋 Próximos passos:"
echo "   1. Faça login no Bradesco"
echo "   2. Vá até BOLETOS REGISTRADOS" 
echo "   3. Execute: python download_simples.py"
