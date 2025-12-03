# Download de Boletos Bradesco - Guia Windows

## 📋 Pré-requisitos

1. **Python 3.8 ou superior**
   - Baixe em: https://www.python.org/downloads/
   - ⚠️ **IMPORTANTE**: Durante a instalação, marque "Add Python to PATH"

2. **Google Chrome**
   - Instale a versão mais recente

## 🚀 Instalação Rápida

### Opção 1: Execução com Duplo-Clique (Recomendado)

1. Baixe todos os arquivos do projeto
2. Dê duplo-clique no arquivo `EXECUTAR_WINDOWS.bat`
3. O script irá:
   - Verificar se Python está instalado
   - Instalar dependências automaticamente
   - Executar o programa

### Opção 2: Instalação Manual

1. Abra o **Prompt de Comando** (cmd) como administrador
2. Navegue até a pasta do projeto:
   ```cmd
   cd C:\caminho\para\download_boleto_viviane
   ```
3. Instale as dependências:
   ```cmd
   pip install -r requirements.txt
   ```
4. Execute o script:
   ```cmd
   python download_boletos_bradesco.py
   ```

## 📝 Como Usar

### Passo a Passo:

1. **Execute o script** (duplo-clique no `.bat` ou via cmd)

2. **O Chrome será aberto automaticamente** no site do Bradesco

3. **Faça login** no Bradesco Net Empresa

4. **Navegue até a página de Boletos Registrados**:
   - Menu → Cobrança → Boletos Registrados → Consultar

5. **Aguarde** a lista de boletos aparecer

6. **Clique em "Verificar Novamente"** na janela do programa

7. **Quando detectar a página correta**, escolha se quer minimizar o navegador

8. **Os boletos serão baixados automaticamente!**

## 🗂️ Onde os Boletos são Salvos?

Por padrão, os boletos são salvos na pasta **Downloads** do Windows:
```
C:\Users\SeuUsuario\Downloads\
```

## ⚙️ Configurações Avançadas

### Alterar Pasta de Downloads:

1. Antes de executar, altere as configurações do Chrome:
   - Abra Chrome → Configurações → Downloads
   - Altere "Local de download"

### Chrome já Aberto (Modo Debug):

Se preferir usar uma sessão do Chrome já aberta:

1. Feche **TODAS** as janelas do Chrome
2. Abra o Prompt de Comando
3. Execute:
   ```cmd
   "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="C:\chrome_debug"
   ```
4. Faça login no Bradesco
5. Execute o script normalmente

## 🛠️ Solução de Problemas

### Erro: "Python não encontrado"
- Reinstale Python e marque "Add Python to PATH"
- Ou adicione manualmente às variáveis de ambiente

### Erro: "Chrome driver incompatível"
- O script baixa automaticamente a versão correta
- Se persistir, atualize o Chrome

### Janela fecha sozinha
- Use o arquivo `EXECUTAR_WINDOWS.bat` (tem `pause` no final)
- Ou execute pelo cmd para ver os erros

### Boletos não são baixados
- Verifique se a página está carregada completamente
- Aguarde alguns segundos antes de clicar em "Verificar Novamente"
- Verifique se o XPath dos elementos não mudou

## 🔧 Desenvolvimento

### Estrutura do Projeto:
```
download_boleto_viviane/
├── download_boletos_bradesco.py  # Script principal
├── requirements.txt               # Dependências
├── EXECUTAR_WINDOWS.bat          # Launcher Windows
├── README.md                      # Documentação geral
└── README_WINDOWS.md             # Este arquivo
```

### Dependências:
- `selenium` - Automação do navegador
- `webdriver-manager` - Gerenciamento automático do ChromeDriver

## 📦 Criar Executável (.exe)

### Com PyInstaller:

1. Instale o PyInstaller:
   ```cmd
   pip install pyinstaller
   ```

2. Crie o executável:
   ```cmd
   pyinstaller --onefile --windowed --add-data "requirements.txt;." download_boletos_bradesco.py
   ```

3. O executável estará em:
   ```
   dist\download_boletos_bradesco.exe
   ```

### Notas sobre o .exe:
- O executável é **maior** (~50MB) pois inclui Python + dependências
- Pode ser detectado como "suspeito" por antivírus (falso positivo)
- Primeira execução é **mais lenta** (descompacta arquivos temporários)

## 🆘 Suporte

### Logs e Debug:

O script mostra mensagens detalhadas no console:
- `[INFO]` - Informações normais
- `[DEBUG]` - Detalhes técnicos
- `[AVISO]` - Avisos importantes
- `[ERRO]` - Erros críticos

### Problemas Comuns:

| Problema | Solução |
|----------|---------|
| "tkinter não encontrado" | Reinstale Python com opção "tcl/tk and IDLE" marcada |
| "Access Denied" | Execute como administrador |
| "Timeout" | Aumente o tempo de espera no código (linha 32) |
| Botão não encontrado | XPath pode ter mudado - verifique com DevTools (F12) |

## 📞 Contato

Para reportar bugs ou sugestões:
- GitHub: https://github.com/Tiburs0/Karangao
- Issues: https://github.com/Tiburs0/Karangao/issues

## 📄 Licença

Este projeto é de uso livre para automação pessoal.
