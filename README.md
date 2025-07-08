# ConectaSalvaAPI

## Visão Geral

A **ConectaSalvaAPI** é uma aplicação Python para automação de consultas e integração de dados entre múltiplos bancos de dados (SQL Server, Azure SQL e OLAP/MDX). Ela executa consultas pré-definidas, centraliza logs de execução e permite salvar resultados diretamente em tabelas SQL Server, facilitando a análise e integração de dados corporativos.

O fluxo principal da API, conforme implementado em `main.py`, executa uma série de consultas estratégicas e salva os resultados de interesse no banco de dados, tornando o processo de atualização e integração de dados mais eficiente e rastreável.

---

## Fluxo Principal (`main.py`)

O arquivo `main.py` executa as seguintes etapas:

1. **Consulta "EXECUCAO DAS DESPESAS ANUAIS"**  
   Executa uma consulta SQL para obter dados de execução de despesas anuais e imprime as primeiras linhas.

2. **Consulta "VALOR AJUSTADO MDX"**  
   Executa uma consulta MDX para obter valores ajustados de um cubo OLAP e imprime as primeiras linhas.

3. **Consulta "VALOR ORIGINAL MDX"**  
   Executa uma consulta MDX para obter valores originais de um cubo OLAP e imprime as primeiras linhas.

4. **Consulta "2214"**  
   Executa uma consulta SQL específica, imprime as primeiras linhas e **salva o resultado na tabela "RECEITAS"** do banco de dados FINANCA.

5. **Consulta "RECEITAS"**  
   Executa uma consulta SQL no Azure para obter dados de receitas e imprime as primeiras linhas.

---

## Estrutura dos Arquivos

```
ConectaSalvaAPI/
│
├── main.py
├── conexao/
│   ├── configura_mdx.py
│   ├── conexoes.py
│   ├── consultas_definidas.py
│   ├── criador_dataframe.py
│   ├── funcoes_globais.py
│   └── utils.py
├── conexao/consultas/
│   ├── email.sql
│   ├── execucao.sql
│   ├── valor_ajustado_25.mdx
│   ├── valor_original_25.mdx
│   ├── 2214.sql
│   └── receitas.sql
└── logs/
    └── execucao_YYYY-MM-DD.log
```

---

## Detalhamento dos Arquivos

- **main.py**  
  Orquestra a execução das consultas e o salvamento dos dados, conforme descrito acima.

- **conexao/configura_mdx.py**  
  Configura o ambiente para execução de consultas MDX, incluindo o carregamento da DLL do Microsoft Analysis Services.

- **conexao/conexoes.py**  
  Define as configurações de conexão para SQL Server, Azure SQL e OLAP.

- **conexao/consultas_definidas.py**  
  Mapeia nomes de consultas para seus scripts SQL/MDX e conexões correspondentes.

- **conexao/criador_dataframe.py**  
  Executa consultas e retorna DataFrames, além de permitir o salvamento de DataFrames no SQL Server.

- **conexao/funcoes_globais.py**  
  Funções para gerenciar conexões, executar consultas por nome, salvar DataFrames e registrar logs.

- **conexao/utils.py**  
  Função utilitária para carregar arquivos SQL/MDX do disco.

- **conexao/consultas/**  
  Scripts SQL e MDX utilizados nas consultas pré-definidas.

- **logs/**  
  Arquivos de log de execução, com data no nome.

---

## Pré-requisitos

- Python 3.8+
- Pacotes: `pandas`, `sqlalchemy`, `pyodbc`, `pyadomd`, `clr-loader` (ou `pythonnet`), `logging`
- Microsoft Analysis Services ADOMD.NET Client (`Microsoft.AnalysisServices.AdomdClient.dll`)
- Drivers ODBC para SQL Server

---

## Instalação

1. **Clone o repositório:**
   ```sh
   git clone <url-do-repositorio>
   cd ConectaSalvaAPI
   ```

2. **Crie e ative um ambiente virtual:**
   ```sh
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Instale as dependências:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Configure o caminho da DLL do ADOMD.NET** em `conexao/configura_mdx.py` se necessário.

5. **Ajuste as conexões** em `conexao/conexoes.py` conforme seu ambiente.

---

## Como Usar

1. **Execute o arquivo principal:**
   ```sh
   python main.py
   ```

2. Os resultados das consultas serão impressos no terminal e logs detalhados serão salvos em `logs/`.

3. Para adicionar novas consultas:
   - Crie o arquivo SQL/MDX em `conexao/consultas/`.
   - Adicione a entrada correspondente em `consultas_definidas.py`.

---

## Observações

- O sistema de logs registra todas as execuções, erros e desempenho.
- O salvamento de DataFrames sobrescreve a tabela destino (`if_exists='replace'`).
- Para consultas MDX, é necessário o ADOMD.NET Client instalado e configurado.

---

## Contato

Dúvidas ou sugestões? Entre em contato com o responsável pelo projeto.
