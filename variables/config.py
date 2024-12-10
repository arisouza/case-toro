import os
from pathlib import Path


############  AMBIENTE
EMAIL_VALIDO = os.getenv("EMAIL")
SENHA = os.getenv("SENHA")

############  DIRETÓRIOS
ROOT = Path(os.path.dirname(os.path.abspath(__file__))).parent

############ PLANILHA DE PRODUTIVIDADE
RELATORIO_TESTES = "Relatório - Testes.xlsx"
PATH_PLANILHA_RESULTADOS = os.path.join(ROOT, 'outputs', RELATORIO_TESTES)
PATH_PLANILHA_RESULTADOS = os.path.normpath(PATH_PLANILHA_RESULTADOS)
RESULTADOS_SHEET_NAME = "Resultados"
METRICAS_SHEET_NAME = "Métricas"
ATENCAO_OPERACIONAL_SHEET_NAME = "Detalhes das Falhas"

LISTA_LINHAS_RESULTADOS = []
LISTA_LINHAS_AT_OP = []
LISTA_LINHAS_METRICAS = []
