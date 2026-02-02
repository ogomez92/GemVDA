# GemVDA - Google Gemini AI para NVDA

## Visao Geral

GemVDA integra as capacidades do Google Gemini AI diretamente no NVDA, fornecendo aos usuarios cegos e com deficiencia visual assistencia de IA poderosa. O complemento suporta varios modelos Gemini incluindo Gemini 3, Gemini 2.5 Pro e variantes Flash para chat, descricao de imagens, analise de video e mais.

## Funcionalidades

* **Chat com IA**: Tenha conversas com Gemini AI diretamente do NVDA
* **Descricao de tela**: Capture e descreva a tela inteira
* **Descricao de objeto**: Descreva o objeto atual do navegador
* **Analise de video**: Grave video da tela e tenha o Gemini analisando-o
* **Anexar imagens**: Anexe imagens de arquivos para descricao por IA
* **Historico de conversa**: Mantenha contexto atraves de multiplas mensagens
* **Multiplos modelos**: Escolha entre varios modelos Gemini baseado nas suas necessidades
* **Configuracoes personalizaveis**: Configure temperatura, tokens, streaming e mais

## Requisitos

* NVDA 2023.1 ou posterior
* Chave API do Google Gemini (nivel gratuito disponivel)
* Conexao com a Internet

## Configuracao

### Obtendo uma chave API

1. Visite [Google AI Studio](https://aistudio.google.com/apikey)
2. Faca login com sua conta Google
3. Crie uma nova chave API
4. Copie a chave para usar no complemento

### Configurando a chave API

1. Pressione NVDA+N para abrir o menu do NVDA
2. Va para Preferencias > Configuracoes
3. Selecione a categoria "Gemini AI"
4. Clique em "Configurar chave API..."
5. Cole sua chave API e pressione OK

## Atalhos de teclado

| Atalho | Acao |
|--------|------|
| NVDA+G | Abrir dialogo do Gemini AI |
| NVDA+Shift+E | Descrever a tela inteira |
| NVDA+Shift+O | Descrever o objeto do navegador |
| NVDA+V | Iniciar/parar gravacao de video para analise |

## Usando o dialogo do Gemini

Quando voce abre o dialogo do Gemini com NVDA+G:

1. **Modelo**: Selecione qual modelo Gemini usar
2. **Prompt do sistema**: Instrucoes opcionais sobre como o Gemini deve responder
3. **Historico**: Visualize o historico da conversa
4. **Mensagem**: Digite sua mensagem ou pergunta
5. **Enviar**: Envie sua mensagem para o Gemini
6. **Anexar imagem**: Adicione um arquivo de imagem para o Gemini analisar
7. **Limpar**: Limpe o historico da conversa
8. **Copiar resposta**: Copie a ultima resposta para a area de transferencia

### Dicas para o dialogo

* Pressione Enter no campo de mensagem para enviar rapidamente
* Use Tab para navegar entre os controles
* O historico atualiza automaticamente enquanto voce conversa
* Imagens anexadas sao enviadas com sua proxima mensagem

## Configuracoes

Acesse as configuracoes via menu NVDA > Preferencias > Configuracoes > Gemini AI:

* **Modelo padrao**: Escolha seu modelo Gemini preferido
* **Temperatura (0-200)**: Controla a criatividade das respostas (0=focado, 200=criativo)
* **Tokens maximos de saida**: Comprimento maximo das respostas
* **Transmitir respostas**: Mostrar respostas conforme chegam
* **Modo conversa**: Incluir historico do chat para contexto
* **Lembrar prompt do sistema**: Salvar seu prompt personalizado
* **Bloquear tecla Escape**: Prevenir fechamento acidental do dialogo
* **Filtrar markdown**: Remover formatacao markdown das respostas

### Feedback sonoro

* **Tocar som ao enviar solicitacao**: Confirmacao de audio quando a mensagem e enviada
* **Tocar som enquanto aguarda**: Som de progresso durante o processamento da IA
* **Tocar som ao receber resposta**: Notificacao quando a resposta chega

## Modelos disponiveis

* **Gemini 3 Pro (Preview)**: Modelo mais capaz com capacidades de raciocinio
* **Gemini 3 Flash (Preview)**: Modelo rapido com capacidades de raciocinio
* **Gemini 2.5 Pro**: Modelo poderoso pronto para producao
* **Gemini 2.5 Flash**: Rapido e eficiente para a maioria das tarefas
* **Gemini 2.5 Flash-Lite**: Leve e respostas mais rapidas
* **Gemini 2.5 Flash Image**: Otimizado para tarefas relacionadas a imagens

## Funcionalidades de imagem e video

### Descricao de tela (NVDA+Shift+E)

Captura sua tela inteira e envia para o Gemini para uma descricao detalhada. Util para:

* Entender interfaces desconhecidas
* Obter uma visao geral do conteudo visual
* Identificar elementos que o NVDA nao consegue descrever

### Descricao de objeto (NVDA+Shift+O)

Captura apenas o objeto atual do navegador. Util para:

* Descrever elementos especificos da interface
* Entender imagens ou icones
* Obter detalhes sobre controles focados

### Analise de video (NVDA+V)

1. Pressione NVDA+V para iniciar a gravacao
2. Execute as acoes que voce quer analisar
3. Pressione NVDA+V novamente para parar
4. Aguarde o Gemini analisar o video

Util para:

* Entender fluxos de trabalho visuais
* Obter descricoes passo a passo
* Analisar conteudo dinamico

## Solucao de problemas

### "Biblioteca Google GenAI nao instalada"

Execute o instalador de dependencias:
1. Navegue ate %APPDATA%\nvda\addons\GemVDA
2. Execute install_deps.bat ou install_deps.py
3. Reinicie o NVDA

### "Nenhuma chave API configurada"

Configure sua chave API em Configuracoes > Gemini AI > Configurar chave API

### Respostas sao muito curtas ou cortadas

Aumente a configuracao "Tokens maximos de saida"

### Respostas sao muito aleatorias

Reduza a configuracao de Temperatura (tente 50-100)

## Nota de privacidade

* Suas mensagens e imagens sao enviadas para a API Gemini do Google
* Chaves API sao armazenadas localmente na sua configuracao do NVDA
* Nenhum dado e compartilhado com o desenvolvedor do complemento
* Revise a politica de privacidade de IA do Google para detalhes

## Suporte

* Relatar problemas: [GitHub Issues](https://github.com/ogomez92/GemVDA/issues)
* Codigo fonte: [GitHub Repository](https://github.com/ogomez92/GemVDA)

## Licenca

Este complemento e lancado sob a Licenca Publica Geral GNU v2.

## Autor

Oriol Gomez Sentis
