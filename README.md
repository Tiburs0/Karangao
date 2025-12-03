# Bradesco Boletos Downloader

Script Python para automatizar o download de boletos do banco Bradesco.

## Pré-requisitos

- Python 3.6 ou superior
- Google Chrome instalado
- ChromeDriver compatível com sua versão do Chrome

## Instalação

1. Instale as dependências:
```bash
pip install -r requirements.txt
```

2. Instale o ChromeDriver:
   - Linux: `sudo apt-get install chromium-chromedriver`
   - Ou baixe de: https://chromedriver.chromium.org/

## Modo de Uso

### Opção 1: Conectar a uma sessão já aberta (Recomendado)

Esta opção permite usar uma sessão do Chrome onde você já está logado.

1. Feche todas as instâncias do Chrome

2. Abra o Chrome em modo debug:
```bash
google-chrome --remote-debugging-port=9222 --user-data-dir="/tmp/chrome_debug"
```

3. Faça login no Bradesco e navegue até a página de boletos

4. Execute o script (veja exemplo abaixo)

### Opção 2: Nova sessão

O script abre uma nova janela do Chrome onde você precisará fazer login manualmente.

## Exemplo de Uso

### Uso Básico (standalone):
```bash
python download_boletos_bradesco.py
```

### Uso como Biblioteca (conectando a sessão existente):
```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from download_boletos_bradesco import BradescoBoletosDownloader

# Conecta ao Chrome em modo debug
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(options=chrome_options)

# Usa o downloader
downloader = BradescoBoletosDownloader(driver)
downloader.baixar_todos_boletos()
```

## Como Funciona

O script:

1. **Conta os boletos**: Verifica quantos boletos estão disponíveis
2. **Para cada boleto**:
   - Clica no botão "Salvar" do boleto
   - Aguarda a nova aba abrir
   - Troca para a nova aba
   - Clica no botão de download
   - Fecha a aba
   - Retorna para a aba principal
3. **Repete** até processar todos os boletos

## XPaths Utilizados

- **Botão do boleto**: `//*[@id="boletoRegistradoDdaForm:listaBoletos_{indice}:Salvar"]`
- **Botão de download**: `//*[@id="formSalvarComo:html"]/span`

## Observações

- O script aguarda até 10 segundos para cada elemento aparecer
- Os downloads vão para a pasta padrão do seu navegador
- Em caso de erro em um boleto, o script continua para o próximo
- Um resumo é exibido ao final com sucessos e falhas

## Troubleshooting

### Erro: ChromeDriver não encontrado
Certifique-se de que o ChromeDriver está instalado e no PATH do sistema.

### Erro: Elemento não encontrado
Verifique se os XPaths estão corretos. O site do banco pode ter mudado.

### Downloads não iniciam
Verifique as configurações de download do Chrome e se há pop-ups bloqueados.

## Licença

MIT
