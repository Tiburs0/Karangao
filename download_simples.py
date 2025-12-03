#!/usr/bin/env python3
"""
Versão SIMPLES e SILENCIOSA do download de boletos.
Trabalha em segundo plano sem atrapalhar.
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from download_boletos_bradesco import BradescoBoletosDownloader


def main():
    print("🔒 Conectando ao Chrome (já aberto por você)...")
    
    try:
        # Conecta ao Chrome que VOCÊ já abriu
        chrome_options = Options()
        chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        
        print(f"✓ Conectado! ({driver.current_url})")
        
        # Minimiza para trabalhar em segundo plano
        print("📦 Minimizando janela...")
        driver.minimize_window()
        
        # Faz o download
        print("⬇️  Iniciando downloads em segundo plano...\n")
        downloader = BradescoBoletosDownloader(driver)
        downloader.baixar_todos_boletos()
        
        print("\n✅ Concluído! Verifique a pasta de Downloads.")
        
    except Exception as e:
        print(f"❌ Erro: {e}")
        print("\n💡 Lembre-se de abrir o Chrome em modo debug primeiro:")
        print("   google-chrome --remote-debugging-port=9222")


if __name__ == "__main__":
    main()
