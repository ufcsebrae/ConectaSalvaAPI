import clr
import os

dll_path = r"C:\Microsoft.AnalysisServices.AdomdClient.dll"

try:
    clr.AddReference(dll_path)
    print("✅ DLL carregada com sucesso!")
except Exception as e:
    print("❌ Erro ao carregar a DLL:")
    print(e)
