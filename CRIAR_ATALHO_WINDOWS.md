# Como criar um atalho no Windows

## Método 1: Atalho para o Script .bat

1. **Localize o arquivo** `EXECUTAR_WINDOWS.bat` na pasta do projeto

2. **Clique com botão direito** no arquivo → **Enviar para** → **Área de trabalho (criar atalho)**

3. **Renomeie o atalho** para "Download Boletos Bradesco"

4. **(Opcional) Adicionar ícone customizado:**
   - Clique direito no atalho → Propriedades
   - Clique em "Alterar ícone"
   - Escolha um ícone do sistema ou use um `.ico` personalizado

5. **Pronto!** Agora pode executar com duplo-clique no atalho

---

## Método 2: Atalho para o Script Python Direto

Se preferir executar o Python diretamente:

1. **Clique direito** na área de trabalho → **Novo** → **Atalho**

2. **Digite o caminho:**
   ```
   C:\Windows\py.exe "C:\caminho\completo\para\download_boletos_bradesco.py"
   ```
   
   ⚠️ Substitua `C:\caminho\completo\para\` pelo caminho real onde está o arquivo

3. **Clique em "Avançar"**

4. **Digite o nome:** `Download Boletos Bradesco`

5. **Clique em "Concluir"**

6. **(Opcional) Configurar o atalho:**
   - Clique direito no atalho → Propriedades
   - **Iniciar em:** `C:\caminho\para\pasta\do\projeto`
   - **Executar:** `Minimizada` (se preferir)
   - **Alterar ícone:** Escolha um ícone

---

## Método 3: Atalho para o Executável (.exe)

Se você criou o executável com PyInstaller:

1. **Localize** `dist\DownloadBoletos.exe`

2. **Clique direito** → **Enviar para** → **Área de trabalho (criar atalho)**

3. **Pronto!** O executável pode ser executado direto, sem precisar do Python instalado

---

## Dicas Extras

### Adicionar ao Menu Iniciar:

1. Copie o atalho criado
2. Cole em: `C:\ProgramData\Microsoft\Windows\Start Menu\Programs\`
3. Ou: `%APPDATA%\Microsoft\Windows\Start Menu\Programs\`

### Fixar na Barra de Tarefas:

1. Clique direito no atalho
2. Selecione "Fixar na barra de tarefas"

### Atalho de Teclado:

1. Clique direito no atalho → Propriedades
2. Em "Tecla de atalho", pressione a combinação desejada
   - Exemplo: `Ctrl + Alt + B`
3. Clique em OK

---

## Solução de Problemas

### "O Windows não consegue encontrar o arquivo"
- Verifique se o caminho está correto
- Use aspas se o caminho tiver espaços
- Use caminho absoluto (completo)

### "Python não é reconhecido"
- Verifique se Python está no PATH
- Use `py.exe` em vez de `python`
- Ou use o caminho completo: `C:\Python311\python.exe`

### Atalho abre e fecha rapidamente
- Use o arquivo `.bat` em vez de `.py`
- Ou adicione `pause` no final do script
- Ou execute pelo cmd para ver erros
