from typing import Dict
from conexao.utils import carregar_sql
from conexao.conexoes import CONEXOES

class Consulta:
    def __init__(self, titulo: str, sql: str, tipo: str, conexao: str):
        self.titulo = titulo
        self.tipo = tipo
        self.sql = sql
        self.conexao = conexao  # ex: "FINANCA" ou "OLAP_SME"

        if conexao not in CONEXOES:
            raise ValueError(f"Conexão '{conexao}' não está definida em CONEXOES.py")

        self.info_conexao = CONEXOES[conexao]  # carrega automaticamente a configuração da conexão

# Dicionário contendo consultas SQL e MDX pré-definidas para uso
consultas: Dict[str, Consulta] = {
  
    "EXECUCAO": Consulta(
        titulo="EXECUÇÃO DAS DESPESAS ANUAIS",
        tipo="sql",
        sql=carregar_sql("conexao/consultas/execucao.sql"),
        conexao="SPSVSQL39"
    ),
    "ValorAjustado25": Consulta(
        titulo="VALOR AJUSTADO MDX",
        tipo="mdx",
        sql=carregar_sql("conexao/consultas/valor_ajustado_25.mdx"),
        conexao="OLAP_SME"
    ),
    "ValorOriginal25": Consulta(
        titulo="VALOR ORIGINAL MDX",
        tipo="mdx",
        sql=carregar_sql("conexao/consultas/valor_original_25.mdx"),
        conexao="OLAP_SME"
    ),
    "2214": Consulta(
        titulo="2214",
        tipo="sql",
        sql=carregar_sql("conexao/consultas/2214.sql"),
        conexao="SPSVSQL39_HubDados"
    ),
    "Receitas": Consulta(
        titulo="Receitas",
        tipo="azure_sql",
        sql=carregar_sql("conexao/consultas/receitas.sql"),
        conexao="AZURE"  # Defina a conexão correta no seu CONEXOES
    )
}