# ConectaSalvaAPI

Este projeto tem como objetivo principal realizar consultas em fontes MDX e salvar os resultados no banco de dados **FINANCA**, permitindo tanto execuções individuais quanto em lote (batch). A arquitetura do projeto é modular e visa facilitar a integração de novas consultas e fluxos de dados.

---

## 📁 Estrutura do Projeto

```
ConectaSalvaAPI/
├── conexao/
│   ├── configura_mdx.py
│   └── funcoes_globais.py
├── main.py
├── main_execucao_batch.py
└── README.md
```

---

## 🚀 Funcionalidade

### 1. `main.py` – Execução de Consulta Única

Permite executar uma consulta específica, visualizar o resultado e salvar os dados no banco de dados FINANCA.

#### Exemplo:
```python
from conexao.configura_mdx import *
from conexao.funcoes_globais import selecionar_consulta_por_nome, salvar_no_financa

query = "RECEITAS"
df = selecionar_consulta_por_nome(query)
print(df.head())
salvar_no_financa(df, "RECEITAS")
```

---

### 2. `main_execucao_batch.py` – Execução em Lote

Executa uma lista de consultas automaticamente, salvando os resultados no banco FINANCA. Também faz logging completo do processo, incluindo início, fim, tempo de execução e falhas.

#### Consultas padrão incluídas:
- RECEITAS
- EXECUCAO DAS DESPESAS ANUAIS
- VALOR AJUSTADO MDX
- VALOR ORIGINAL MDX

#### Execução:
```bash
python main_execucao_batch.py
```

#### Saída esperada:
O sistema logará a execução de cada consulta, salvando os resultados com informações detalhadas sobre possíveis erros.

---

## 🛠️ Dependências

As dependências principais do projeto são:

- `pandas`
- `pyodbc` ou `sqlalchemy` (dependendo da conexão com o FINANCA)
- `logging`
- `datetime`

Certifique-se de configurar corretamente o arquivo `conexao/configura_mdx.py` com as credenciais e parâmetros para acesso aos cubos MDX.

---

## 📌 Observações

- Use `main.py` para testes individuais e validações pontuais.
- Use `main_execucao_batch.py` para rotinas automáticas e processos agendados.
- Adapte a lista `consultas_para_rodar` no `main_execucao_batch.py` conforme necessário, adicionando ou removendo títulos de consultas.
- Adicone novas consultas na pasta `conexao/consultas`
- Atualize o dicionário em `conexao/conexoes.py`, para adicionar novas conexões.
- Atualize o dicionário em `conexao/consultas_definidas.py` para relacionar conexões e consultas.
- Atualize o CASE/WHEN em `conexao/funcoes_globais.py` para relacionar chamar as consultas pelo título.

---

## 📄 Licença

Este repositório está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
