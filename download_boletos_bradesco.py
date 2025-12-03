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
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
import tkinter as tk
from tkinter import messagebox


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
            # Caso não tenha um driver, cria um novo com webdriver-manager
            service = Service(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=service)
        
        self.wait = WebDriverWait(self.driver, 10)
        self.janela_principal = None
    
    def contar_boletos(self):
        """
        Conta quantos boletos estão disponíveis para download.
        
        Returns:
            int: Número de boletos encontrados
        """
        print("\n[DEBUG] Iniciando contagem de boletos...")
        print(f"[DEBUG] URL atual: {self.driver.current_url}")
        print(f"[DEBUG] Título da página: {self.driver.title}")
        
        # Verifica se está na página correta
        if "boletoRegistrado" not in self.driver.current_url:
            print("\n[AVISO] ⚠️  Você NÃO está na página de boletos!")
            print(f"[AVISO] URL atual: {self.driver.current_url}")
            print("[AVISO] URL esperada deve conter: 'boletoRegistrado'")
            print("\n[DICA] Navegue até a página de boletos antes de continuar.")
            return 0
        
        contador = 0
        while True:
            try:
                xpath = f'//*[@id="boletoRegistradoDdaForm:listaBoletos_{contador}:Salvar"]'
                print(f"[DEBUG] Procurando boleto {contador} com XPath: {xpath}")
                elemento = self.driver.find_element(By.XPATH, xpath)
                if elemento:
                    print(f"[DEBUG] ✓ Boleto {contador} encontrado!")
                    contador += 1
            except NoSuchElementException:
                print(f"[DEBUG] ✗ Boleto {contador} não encontrado. Parando contagem.")
                break
        
        print(f"\n[RESULTADO] Total de boletos encontrados: {contador}")
        
        if contador == 0:
            print("\n[AVISO] Nenhum boleto encontrado!")
            print("[DEBUG] HTML da página (primeiros 500 caracteres):")
            print(self.driver.page_source[:500])
            print("\n[DEBUG] Tentando encontrar elementos com ID similar:")
            try:
                elementos = self.driver.find_elements(By.XPATH, "//*[contains(@id, 'boleto')]")
                print(f"[DEBUG] Encontrados {len(elementos)} elementos com 'boleto' no ID:")
                for elem in elementos[:5]:  # Mostra apenas os 5 primeiros
                    print(f"  - ID: {elem.get_attribute('id')}")
            except Exception as e:
                print(f"[DEBUG] Erro ao buscar elementos: {e}")
        
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
            try:
                self.driver.switch_to.window(self.janela_principal)
            except:
                pass
            return False
        except Exception as e:
            print(f"  ✗ Erro ao processar boleto {indice + 1}: {str(e)}")
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
    Abre o Chrome automaticamente no site do Bradesco.
    """
    print("=" * 60)
    print("Download de Boletos Bradesco")
    print("=" * 60)
    
    try:
        print("\n[INFO] Abrindo Chrome no site do Bradesco...")
        
        from selenium.webdriver.chrome.options import Options
        import os
        
        chrome_options = Options()
        chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        
        service = Service(ChromeDriverManager().install())
        
        try:
            # Tenta conectar a uma sessão existente primeiro
            driver = webdriver.Chrome(service=service, options=chrome_options)
            print("[INFO] ✓ Conectado ao Chrome existente")
        except:
            # Se não conseguir, abre um novo Chrome
            print("[INFO] Abrindo novo navegador...")
            chrome_options = Options()
            chrome_options.add_argument("--start-maximized")
            driver = webdriver.Chrome(service=service, options=chrome_options)
            
            # Navega para o site do Bradesco
            print("[INFO] Acessando site do Bradesco...")
            driver.get("https://www.ne12.bradesconetempresa.b.br/ibpjlogin/login.jsf")
            
            # Aguarda a página carregar
            time.sleep(3)
            print("[INFO] ✓ Site carregado!")
        
        # Cria janela de confirmação gráfica
        root = tk.Tk()
        root.withdraw()  # Esconde a janela principal
        
        # Loop até estar na página correta
        while True:
            # Verifica se o navegador ainda está aberto
            try:
                # Tenta pegar todas as janelas abertas
                janelas = driver.window_handles
                if not janelas:
                    raise Exception("Nenhuma janela aberta")
                
                # Se a janela atual foi fechada, troca para qualquer janela disponível
                try:
                    url_atual = driver.current_url or ""
                except:
                    # Janela atual foi fechada, troca para a primeira disponível
                    driver.switch_to.window(janelas[0])
                    url_atual = driver.current_url or ""
                
                titulo_atual = driver.title or ""
            except Exception as e:
                messagebox.showerror(
                    "Erro",
                    "O navegador foi fechado!\n\n"
                    "Por favor, execute o script novamente e não feche o navegador."
                )
                print(f"\n[ERRO] Navegador foi fechado: {e}")
                return
            
            # Verifica se já está na página de boletos
            if "boletoRegistrado" in url_atual:
                # Já está na página correta!
                resposta = messagebox.askyesno(
                    "Página Correta Detectada!",
                    f"✓ Você JÁ está na página de boletos!\n\n"
                    f"URL: {url_atual[:60]}...\n"
                    f"Título: {titulo_atual}\n\n"
                    f"Deseja iniciar o download agora?",
                    icon='info'
                )
                
                if resposta:
                    print(f"\n[INFO] ✓ Página de boletos detectada!")
                    print(f"[INFO] URL: {url_atual}")
                    break
                else:
                    print("\n[INFO] Operação cancelada pelo usuário.")
                    try:
                        driver.quit()
                    except:
                        pass
                    return
            else:
                # Não está na página de boletos - mostra instruções
                mensagem = (
                    "VOCÊ NÃO ESTÁ NA PÁGINA DE BOLETOS!\n\n"
                    f"📍 URL atual:\n{url_atual[:80]}\n\n"
                    f"📄 Título: {titulo_atual}\n\n"
                    "INSTRUÇÕES:\n\n"
                    "1. Faça login no Bradesco (se necessário)\n"
                    "2. Navegue até BOLETOS REGISTRADOS\n"
                    "3. Aguarde a lista de boletos aparecer\n"
                    "4. Clique em 'Verificar Novamente'\n\n"
                    "⚠️ NÃO FECHE O NAVEGADOR!"
                )
                
                resposta = messagebox.askretrycancel(
                    "Navegue até a Página de Boletos",
                    mensagem,
                    icon='warning'
                )
                
                if not resposta:
                    print("\n[INFO] Operação cancelada pelo usuário.")
                    try:
                        driver.quit()
                    except:
                        pass
                    return
                
                # Usuário clicou em "Verificar Novamente" - loop continua
                print("[INFO] Verificando URL novamente...")
                time.sleep(1)
        
        # Pergunta se quer minimizar a janela
        minimizar = messagebox.askyesno(
            "Minimizar Navegador",
            "Deseja minimizar a janela do navegador durante o processo?\n\n"
            "(Recomendado para não atrapalhar seu trabalho)",
            icon='question'
        )
        
        if minimizar:
            try:
                driver.minimize_window()
                print("[INFO] ✓ Janela minimizada")
            except Exception as e:
                print(f"[AVISO] Não foi possível minimizar: {e}")
        
        print("\n[INFO] Iniciando processo de download...\n")
        
        downloader = BradescoBoletosDownloader(driver)
        downloader.baixar_todos_boletos()
        
        # Mostra resultado final
        messagebox.showinfo(
            "Concluído!",
            "Download de boletos finalizado!\n\n"
            "O navegador permanecerá aberto.\n"
            "Verifique os arquivos baixados na pasta de Downloads."
        )
        
        print("\n[INFO] Processo finalizado!")
        print("[INFO] O navegador permanecerá aberto.")
        
    except Exception as e:
        print(f"\n[ERRO] {str(e)}")
        messagebox.showerror(
            "Erro",
            f"Ocorreu um erro:\n\n{str(e)}\n\n"
            "Verifique o console para mais detalhes."
        )
        import traceback
        print("\n[DEBUG] Traceback completo:")
        traceback.print_exc()


if __name__ == "__main__":
    main()
