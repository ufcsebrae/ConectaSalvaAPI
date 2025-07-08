from conexao.configura_mdx import *
from conexao.funcoes_globais import selecionar_consulta_por_nome, salvar_no_financa, logger
from datetime import datetime


def executar_batch(titulos_consultas: list):
    """
    Executa um lote de consultas e salva os resultados.
    Loga todo o processo com tempos, erros e estatísticas.
    """
    logger.info(f"\n🚀 Início da execução batch em {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")

    for titulo in titulos_consultas:
        try:
            logger.info(f"\n🔄 Processando consulta: '{titulo}'")
            df = selecionar_consulta_por_nome(titulo)
            salvar_no_financa(df, titulo)
        except Exception as e:
            logger.error(f"❌ Falha inesperada ao processar '{titulo}': {e}")

    logger.info(f"\n🏁 Fim da execução batch em {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n")

# Execução real do batch
if __name__ == "__main__":
    consultas_para_rodar = [
        "RECEITAS",
        "EXECUCAO DAS DESPESAS ANUAIS",
        "VALOR AJUSTADO MDX",
        "VALOR ORIGINAL MDX"
    ]
    executar_batch(consultas_para_rodar)
