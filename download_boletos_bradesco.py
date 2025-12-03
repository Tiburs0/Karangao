#!/usr/bin/env python3
"""
Script para automatizar o download de boletos do Bradesco.
Executa quando o usuário já está com o site do banco aberto.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time


class BradescoBoletosDownloader:
    def __init__(self, driver=None):
        """
        Inicializa o downloader.
        
        Args:
            driver: Instância do WebDriver já existente (opcional)
        """
        if driver:
            self.driver = driver
        else:
            # Caso não tenha um driver, cria um novo
            self.driver = webdriver.Chrome()
        
        self.wait = WebDriverWait(self.driver, 10)
        self.janela_principal = None
    
    def contar_boletos(self):
        """
        Conta quantos boletos estão disponíveis para download.
        
        Returns:
            int: Número de boletos encontrados
        """
        contador = 0
        while True:
            try:
                xpath = f'//*[@id="boletoRegistradoDdaForm:listaBoletos_{contador}:Salvar"]'
                elemento = self.driver.find_element(By.XPATH, xpath)
                if elemento:
                    contador += 1
            except NoSuchElementException:
                break
        
        print(f"Total de boletos encontrados: {contador}")
        return contador
    
    def baixar_boleto(self, indice):
        """
        Baixa um boleto específico pelo índice.
        
        Args:
            indice: Índice do boleto (começando em 0)
        """
        try:
            print(f"Processando boleto {indice + 1}...")
            
            # Guarda a janela principal
            if self.janela_principal is None:
                self.janela_principal = self.driver.current_window_handle
            
            # Clica no botão do boleto
            xpath_boleto = f'//*[@id="boletoRegistradoDdaForm:listaBoletos_{indice}:Salvar"]'
            botao_boleto = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, xpath_boleto))
            )
            botao_boleto.click()
            print(f"  ✓ Clicou no boleto {indice + 1}")
            
            # Aguarda a nova aba abrir
            time.sleep(2)
            
            # Troca para a nova aba
            janelas = self.driver.window_handles
            for janela in janelas:
                if janela != self.janela_principal:
                    self.driver.switch_to.window(janela)
                    break
            
            print(f"  ✓ Trocou para a aba de download")
            
            # Clica no botão de download
            xpath_download = '//*[@id="formSalvarComo:html"]/span'
            botao_download = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, xpath_download))
            )
            botao_download.click()
            print(f"  ✓ Iniciou o download")
            
            # Aguarda o download iniciar
            time.sleep(2)
            
            # Fecha a aba atual
            self.driver.close()
            print(f"  ✓ Fechou a aba de download")
            
            # Volta para a janela principal
            self.driver.switch_to.window(self.janela_principal)
            print(f"  ✓ Retornou para a janela principal")
            
            # Aguarda um pouco antes do próximo
            time.sleep(1)
            
            return True
            
        except TimeoutException:
            print(f"  ✗ Timeout ao processar boleto {indice + 1}")
            return False
        except Exception as e:
            print(f"  ✗ Erro ao processar boleto {indice + 1}: {str(e)}")
            # Tenta voltar para a janela principal em caso de erro
            try:
                self.driver.switch_to.window(self.janela_principal)
            except:
                pass
            return False
    
    def baixar_todos_boletos(self):
        """
        Baixa todos os boletos disponíveis.
        """
        print("=" * 60)
        print("Iniciando download de boletos do Bradesco")
        print("=" * 60)
        
        # Conta os boletos
        total_boletos = self.contar_boletos()
        
        if total_boletos == 0:
            print("Nenhum boleto encontrado!")
            return
        
        print(f"\nIniciando download de {total_boletos} boleto(s)...\n")
        
        # Baixa cada boleto
        sucesso = 0
        falhas = 0
        
        for i in range(total_boletos):
            if self.baixar_boleto(i):
                sucesso += 1
            else:
                falhas += 1
            print()  # Linha em branco
        
        # Resumo
        print("=" * 60)
        print("Download concluído!")
        print(f"Total: {total_boletos} | Sucesso: {sucesso} | Falhas: {falhas}")
        print("=" * 60)


def main():
    """
    Função principal para executar o script standalone.
    """
    print("ATENÇÃO: Certifique-se de que:")
    print("1. O ChromeDriver está instalado")
    print("2. Você já está logado no site do Bradesco")
    print("3. Está na página de boletos")
    print()
    
    input("Pressione ENTER para continuar...")
    
    # Para usar com uma sessão já aberta, você precisa conectar ao Chrome em modo debug
    # Inicie o Chrome com: chrome --remote-debugging-port=9222
    # E use o código abaixo:
    
    # from selenium.webdriver.chrome.options import Options
    # chrome_options = Options()
    # chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    # driver = webdriver.Chrome(options=chrome_options)
    
    # Para este exemplo, vamos criar um novo driver
    # Você deve adaptar conforme sua necessidade
    
    try:
        downloader = BradescoBoletosDownloader()
        
        print("\nAguardando você navegar até a página de boletos...")
        print("Pressione ENTER quando estiver pronto...")
        input()
        
        downloader.baixar_todos_boletos()
        
        print("\nProcesso finalizado!")
        input("Pressione ENTER para fechar o navegador...")
        
    except Exception as e:
        print(f"Erro: {str(e)}")
    finally:
        try:
            downloader.driver.quit()
        except:
            pass


if __name__ == "__main__":
    main()
