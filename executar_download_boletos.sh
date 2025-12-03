#!/bin/bash
# Script simples para executar o download de boletos do Bradesco

cd /home/jm/github/Karangao_download_boleto
python3 download_boletos_bradesco.py

# Aguarda o usuário pressionar ENTER antes de fechar
echo ""
echo "Pressione ENTER para fechar..."
read
