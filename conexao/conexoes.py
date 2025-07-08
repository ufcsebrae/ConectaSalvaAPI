CONEXOES = {
    "SPSVSQL39": {
        "tipo": "sql",
        "servidor": "spsvsql39\\metas",
        "banco": "FINANCA",
        "driver": "ODBC+Driver+17+for+SQL+Server",
        "trusted_connection": True
    },
        "SPSVSQL39_HubDados": {
        "tipo": "sql",
        "servidor": "spsvsql39\\metas",
        "banco": "HubDados",
        "driver": "ODBC+Driver+17+for+SQL+Server",
        "trusted_connection": True
    },
    "OLAP_SME": {
        "tipo": "olap",
        "str_conexao": "Provider=MSOLAP;Data Source=10.1.100.167;Catalog=SMEDW_V3_SSAS;",
    },
    "AZURE": {
        "tipo": "azure_sql",
        "servidor": "synapsesebraespprod-ondemand.sql.azuresynapse.net",
        "banco": "DatamartMeta",
        "driver": "ODBC+Driver+17+for+SQL+Server",
        "authentication": "ActiveDirectoryInteractive"
    }   
}