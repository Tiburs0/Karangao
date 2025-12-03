#!/usr/bin/env python3
"""
Exemplo de uso do downloader conectando a uma sessão já aberta do Chrome.

Para usar este script:
1. Feche todas as instâncias do Chrome
2. Abra o Chrome em modo debug:
   google-chrome --remote-debugging-port=9222 --user-data-dir="/tmp/chrome_debug"
3. Faça login no Bradesco e vá até a página de boletos
4. Execute este script
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from download_boletos_bradesco import BradescoBoletosDownloader


def main():
    print("=" * 60)
    print("Conectando ao Chrome existente...")
    print("=" * 60)
    
    try:
        # Configura opções para conectar ao Chrome em modo debug
        chrome_options = Options()
        chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        
        # Conecta ao Chrome usando webdriver-manager
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        print("✓ Conectado com sucesso!")
        print(f"✓ URL atual: {driver.current_url}")
        print()
        
        # Verifica se está na página correta
        if "bradesco" not in driver.current_url.lower():
            print("AVISO: Você não parece estar no site do Bradesco")
            print("Certifique-se de estar na página de boletos antes de continuar")
            print()
        
        input("Pressione ENTER para iniciar o download dos boletos...")
        print()
        
        # Cria o downloader e baixa os boletos
        downloader = BradescoBoletosDownloader(driver)
        downloader.baixar_todos_boletos()
        
        print("\n✓ Processo concluído!")
        print("NOTA: O navegador permanecerá aberto.")
        
    except Exception as e:
        print(f"✗ Erro: {str(e)}")
        print()
        print("Certifique-se de que:")
        print("1. O Chrome foi iniciado com --remote-debugging-port=9222")
        print("2. O ChromeDriver está instalado")
        print("3. A versão do ChromeDriver é compatível com seu Chrome")


if __name__ == "__main__":
    main()
