# Planilha_Web
Pegar os dados de uma planilha  Excel e mostrar em uma página Web,utilizando Python no back-end.

**Descrição Geral:**

O código apresenta uma aplicação web construída com o framework Flask, que exibe uma tabela HTML renderizada a partir de um arquivo Excel. Além disso, há a criação de uma planilha Excel contendo dados fictícios de produtos. A estrutura inclui duas partes distintas: a primeira é responsável pela configuração do servidor Flask e a renderização da tabela HTML, enquanto a segunda gera dados fictícios de produtos, cria um DataFrame Pandas e salva esses dados em um arquivo Excel.

**Classes e Métodos:**

1. **Classe: `FlaskApp` (Flask)**
   
   - **Método: `__init__`**
   
     Inicializa a aplicação Flask.

   - **Método: `index` (rota '/')**
   
     Define a rota inicial que lê um arquivo Excel, converte-o para uma tabela HTML e renderiza uma página usando um template HTML.

   - **Método: `__main__`**
   
     Inicia o servidor Flask quando o script é executado diretamente.

2. **Criação de Dados Fictícios (fora da classe Flask)**

   - **Método: `create_fictional_products`**
   
     Gera dados fictícios de produtos, como ID, Nome do Produto, Preço e Quantidade em Estoque.

   - **Método: `create_dataframe`**
   
     Cria um DataFrame Pandas a partir dos dados fictícios gerados.

   - **Método: `save_to_excel`**
   
     Salva o DataFrame em um arquivo Excel.

3. **Template HTML (`index.html`)**

   - **Elemento: `table_html`**
   
     Exibe a tabela HTML gerada a partir do DataFrame Pandas.

   - **Condição: `{% if table_html %}`**
   
     Verifica se há dados para exibir na tabela.

   - **Script: `<script src="{{ url_for('static', filename='js/index.js') }}"></script>`**
   
     Importa um script JavaScript (não fornecido no código) para possível interatividade futura.

   - **Estilo: `<link rel="stylesheet" href="{{ url_for('static', filename='css/index.css') }}">`**
   
     Adiciona um arquivo de estilo para estilizar a página.

4. **Salvar Dados em Excel**

   - **Método: `to_excel`**
   
     Salva o DataFrame em um arquivo Excel chamado '_tabela.xlsx' no diretório 'static/sheets/'.

   - **Mensagem: `print("Arquivo '_tabela.xlsx' criado com sucesso.")`**
   
     Imprime uma mensagem indicando o sucesso da criação do arquivo Excel.

