# Aplicação Flask de Vendas

Esta aplicação Flask permite que os usuários façam upload de arquivos CSV contendo dados de vendas, que são armazenados em um banco de dados SQLite. Além disso, a aplicação fornece uma API para consulta de dados de vendas, um relatório de análise básica e a geração de relatórios diários em PDF.

## Sumário
1. [Instalação](#instalação)
2. [Configuração do Banco de Dados](#configuração-do-banco-de-dados)
3. [Rotas da API](#rotas-da-api)
4. [Funcionalidades](#funcionalidades)
5. [Testes](#testes)
6. [Execução](#execução)

---

## Instalação

1. **Clone o Repositório**:
   ```bash
   git clone https://github.com/seu-usuario/sua-aplicacao-flask.git
   cd sua-aplicacao-flask
   ```
2. **Crie um Ambiente Virtual**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Para Linux/Mac
   venv\Scripts\activate     # Para Windows
   ```

3. **Instale as Dependências**:
   ```bash
   pip install -r requirements.txt
   ```

## **Configuração do Banco de Dados**

A aplicação utiliza o SQLite como banco de dados padrão. Para configurar o banco de dados, execute:
   ```bash
   flask db upgrade
   ```

Esse comando criará o banco de dados com as tabelas necessárias.

## **Rotas da API**
<table>
   <thead>
      <th>Método</th>
      <th>Endpoint</th>
      <th>Descrição</th>
   </thead>

   <tr>
      <td>GET</td>
      <td>/</td>
      <td>Página principal com formulário de upload de CSV.</td>
   </tr>

   <tr>
      <td>POST</td>
      <td>/upload_csv</td>
      <td>Recebe o arquivo CSV e armazena os dados no banco de dados.</td>
   </tr>

   <tr>
      <td>GET</td>
      <td>/report</td>
      <td>Exibe o relatório de vendas e análises no navegador.</td>
   </tr>

   <tr>
      <td>GET</td>
      <td>/generate_daily_report</td>
      <td>Gera um relatório diário das vendas em PDF.</td>
   </tr>

   <tr>
      <td>GET</td>
      <td>/get_sales</td>
      <td>API para consulta de dados de vendas paginados.</td>
   </tr>
</table>

## Exemplo de Requisição para ```/get_sales```
   <ul>
      <li><strong>GET</strong> /get_sales?page=1</li>
   </ul>

   **Resposta**
   ```json
   {
      "sales": [
         {
            "id": 1,
            "date": "2024-09-20",
            "customer_name": "Julia Santos",
            "product": "Impressora",
            "quantity": 3,
            "unit_price": 600,
            "total_sale": 1800
         },
         ...
      ]
   }
   ```

## Funcionalidades

1. **Upload de CSV**:
   <ul>
      <li>Faça upload de um arquivo CSV contendo os dados de vendas. A aplicação processa e armazena os dados no banco de dados.</li>
      <li>O arquivo CSV deve ter as seguintes colunas: ID_Venda, Data_Venda, ID_Cliente, Nome_Cliente, Produto, Quantidade, Preco_Unitario, Total_Venda.</li>
   </ul>

2. **Análise de Vendas**:
   
   A função analyze_sales calcula métricas de vendas, incluindo:
   <ul>
      <li>Total de Vendas (R$): Soma dos valores das vendas.</li>
      <li>Total de Produtos Vendidos: Quantidade total de produtos vendidos.</li>
      <li>Ticket Médio: Valor médio gasto por venda.</li>
      <li>Produto Mais Vendido: Produto com maior quantidade de vendas.</li>
   </ul>

3. **Geração de Relatório PDF**:
   <ul>
      <li>Acesse a rota /generate_daily_report para gerar e baixar um relatório em PDF com as informações diárias de vendas.</li>
   </ul>

## Testes

1. **Configuração**:
   <ul>
      <li>A aplicação usa pytest para testes unitários. Para garantir que o pytest encontre o módulo app, configure o PYTHONPATH:</li>
   </ul>

   ```bash
   PYTHONPATH=. pytest
   ```

2. **Principais Testes**:
   
   A função analyze_sales calcula métricas de vendas, incluindo:
   <ul>
      <li>test_upload_csv: Verifica se o upload de arquivo CSV funciona corretamente</li>
      <li>test_analyze_sales: Testa a análise básica dos dados de vendas.</li>
      <li>test_api_get_sales: Garante que a API de listagem de vendas retorna os dados em JSON corretamente.</li>
      <li>test_generate_daily_report: Confirma que a geração de PDF é bem-sucedida.</li>
      <li>test_report_page: Verifica se a página de relatório é carregada com sucesso.</li>
   </ul>

## Execução

1. **Iniciar a Aplicação**:
   
   Para iniciar a aplicação Flask em modo de desenvolvimento, use:
   ```bash
   flask run
   ```
   A aplicação estará disponível em http://127.0.0.1:5000.

2. **Executar Testes**:
   
   Para rodar todos os testes:
   ```bash
   pytest
   ```
   A aplicação estará disponível em http://127.0.0.1:5000.
