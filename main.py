from conexao.configura_mdx import *
from conexao.funcoes_globais import selecionar_consulta_por_nome,salvar_no_financa

def main():
    ##query = "EXECUCAO DAS DESPESAS ANUAIS"
    ##dfEXECUCAO = selecionar_consulta_por_nome(query)
    ##print(dfEXECUCAO.head())

    ##query = "VALOR AJUSTADO MDX"
    ##dfVALORAJUSTADO25 = selecionar_consulta_por_nome(query)
    ##print(dfVALORAJUSTADO25.head())

    ##query = "VALOR ORIGINAL MDX"
    ##dfVALORORIGINAL25 = selecionar_consulta_por_nome(query)
    ##print(dfVALORORIGINAL25.head())
    
    ##query = "2214"
    ##df2214 = selecionar_consulta_por_nome(query)
    ##salvar_no_financa(df2214, "2214")
    ##print(df2214.head())
   
    query = "RECEITAS"
    dfRECEITAS = selecionar_consulta_por_nome(query)
    print(dfRECEITAS.head())
    salvar_no_financa(dfRECEITAS, "RECEITAS") 
    ##use -- salvar_no_financa(dfReceitas, "RECEITAS") para salvar no banco de dados FINANCA
    
if __name__ == "__main__":
    main()
