# Bradesco Boletos Downloader

Script Python para automatizar o download**Opção 2: Conectar a Chrome Existente**

Esta opção permite usar uma sessão do Chrome onde você já está logado.

1. Feche todas as instâncias do Chrome

2. **Windows**: Abra o Chrome em modo debug:
```cmd
"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="C:\chrome_debug"
```

   **Linux**: Abra o Chrome em modo debug:
```bash
google-chrome --remote-debugging-port=9222 --user-data-dir="/tmp/chrome_debug"
```

3. Faça login no Bradesco e navegue até a página de boletos

4. Execute o script normalmente

## 🔗 Criar Atalhos

### Windows
Veja instruções detalhadas em [CRIAR_ATALHO_WINDOWS.md](CRIAR_ATALHO_WINDOWS.md)

**Resumo:**
- Clique direito em `EXECUTAR_WINDOWS.bat` → Enviar para → Área de trabalho
- Ou use o executável `.exe` gerado

### Linux
```bash
# Criar atalho na área de trabalho
cp download_boletos_bradesco.desktop ~/Desktop/
chmod +x ~/Desktop/download_boletos_bradesco.desktop
```

## 🖥️ Compatibilidade

- ✅ **Windows** (Windows 10/11)
- ✅ **Linux** (Ubuntu, Debian, etc.)
- ✅ **macOS** (não testado, mas deve funcionar)

## 📋 Pré-requisitos

- Python 3.8 ou superior
- Google Chrome instalado
- Conexão com internet (para baixar ChromeDriver automaticamente)

## 📖 Documentação por Sistema

- **Windows**: Leia [README_WINDOWS.md](README_WINDOWS.md) para instruções detalhadas
- **Linux**: Continue lendo este arquivo

## 🚀 Instalação

### Windows

**Método Rápido (Recomendado):**
1. Dê duplo-clique em `EXECUTAR_WINDOWS.bat`
2. O script instalará tudo automaticamente!

**Método Manual:**
```cmd
pip install -r requirements.txt
```

### Linux

```bash
pip install -r requirements.txt
```

**Nota**: O ChromeDriver é baixado automaticamente pelo `webdriver-manager`

## 🎯 Modo de Uso

### 🪟 Windows

**Opção 1: Duplo-Clique (Mais Fácil)**
1. Execute `EXECUTAR_WINDOWS.bat`
2. O Chrome abrirá automaticamente
3. Faça login no Bradesco
4. Navegue até "Boletos Registrados"
5. Aguarde a janela do programa detectar automaticamente!

**Opção 2: Criar Executável**
1. Execute `BUILD_EXE.bat`
2. Use o arquivo `.exe` gerado em `dist/`

**Opção 3: Linha de Comando**
```cmd
python download_boletos_bradesco.py
```

### 🐧 Linux

**Opção 1: Script Automático (Recomendado)**
```bash
python3 download_boletos_bradesco.py
```
O Chrome abrirá automaticamente!

**Opção 2: Conectar a Chrome Existente**

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

## 📁 Estrutura do Projeto

```
download_boleto_viviane/
├── download_boletos_bradesco.py   # Script principal ⭐
├── requirements.txt               # Dependências Python
├── README.md                      # Este arquivo
├── README_WINDOWS.md             # Guia detalhado Windows
│
├── EXECUTAR_WINDOWS.bat          # Launcher Windows 🪟
├── BUILD_EXE.bat                 # Criar executável Windows
├── CRIAR_ATALHO_WINDOWS.md       # Tutorial de atalhos Windows
│
├── 1_abrir_chrome_debug.sh       # Helper Linux 🐧
├── COMO_USAR.sh                  # Guia interativo Linux
├── modo_invisivel.sh             # Execução com Xvfb (Linux)
│
└── exemplo_uso_chrome_debug.py   # Exemplo de uso como biblioteca
```

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
