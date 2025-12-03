#!/usr/bin/env python3
"""
Exemplo avançado com opção de minimizar ou ocultar a janela do navegador.
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from download_boletos_bradesco import BradescoBoletosDownloader


def main():
    print("=" * 60)
    print("Download de Boletos Bradesco - Modo Discreto")
    print("=" * 60)
    
    print("\nEscolha o modo de operação:")
    print("1. Normal (janela visível)")
    print("2. Minimizada (janela na barra de tarefas)")
    print("3. Segundo plano (menos recursos, mas visível se você mudar de aba)")
    
    modo = input("\nDigite o número da opção (1, 2 ou 3): ").strip()
    
    try:
        print("\n[INFO] Conectando ao Chrome...")
        
        chrome_options = Options()
        chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        
        # Opções adicionais para modo discreto
        if modo == "3":
            # Reduz o uso de recursos
            chrome_options.add_argument("--disable-gpu")
            chrome_options.add_argument("--disable-software-rasterizer")
            chrome_options.add_argument("--disable-dev-shm-usage")
        
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        
        # Aplica o modo escolhido
        if modo == "2":
            driver.minimize_window()
            print("[INFO] ✓ Janela minimizada")
        elif modo == "3":
            # Define tamanho pequeno e move para canto
            driver.set_window_size(800, 600)
            driver.set_window_position(0, 0)
            print("[INFO] ✓ Janela reduzida e posicionada")
        else:
            print("[INFO] ✓ Modo normal")
        
        print(f"[INFO] ✓ Conectado!")
        print(f"[INFO] URL: {driver.current_url}")
        
        # Verifica se está na página de boletos
        if "boletoRegistrado" not in driver.current_url:
            print("\n⚠️  Você não está na página de boletos!")
            print("📋 Navegue até a página de boletos no Chrome")
            input("Pressione ENTER quando estiver pronto...")
        
        print("\n[INFO] Iniciando download...\n")
        
        downloader = BradescoBoletosDownloader(driver)
        downloader.baixar_todos_boletos()
        
        print("\n[INFO] ✓ Concluído!")
        print("[INFO] O navegador permanecerá aberto.")
        
    except Exception as e:
        print(f"\n[ERRO] {str(e)}")
        print("\n[DICA] Certifique-se de que o Chrome está em modo debug:")
        print("  google-chrome --remote-debugging-port=9222 --user-data-dir=\"/tmp/chrome_debug\"")


if __name__ == "__main__":
    main()
