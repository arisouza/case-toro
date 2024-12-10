import traceback
from datetime import datetime
import pandas as pd
from robot.api import logger
from robot.libraries.BuiltIn import BuiltIn
from variables.config import (
    RELATORIO_TESTES,
    PATH_PLANILHA_RESULTADOS,
    RESULTADOS_SHEET_NAME,
    ATENCAO_OPERACIONAL_SHEET_NAME,
    METRICAS_SHEET_NAME,
    LISTA_LINHAS_RESULTADOS,
    LISTA_LINHAS_AT_OP,
    LISTA_LINHAS_METRICAS,
)


class RelatorioProdutividade:
    """Classe para manipulação da planilha de produtividade."""

    def __init__(self):
        self.planilha_obj = self.capturar_planilha_excel()

    def criar_linha_de_detalhes_da_falha(self, detalhe_erro):
        """
        Cria uma linha de dados para registro de detalhes da falha.

        :param detalhe_erro: Detalhe do erro encontrado.
        """
        data = datetime.now().strftime("%d/%m/%Y %H:%H:%M:%S")
        suite = BuiltIn().get_variable_value("${SUITE_NAME}", "")
        cenario = BuiltIn().get_variable_value("${TEST_NAME}", "")
        linha = [data, suite, cenario, detalhe_erro]
        LISTA_LINHAS_AT_OP.append(linha)

    def criar_linha_de_resultado(self, resultado, tempo_execucao):
        """Cria uma linha de resultado para o relatório de produtividade.

        :param mensagem: Mensagem que será utilizada para criar a linha de resultado.
        :type mensagem: str
        :param dict_processo: Dicionário contendo os dados do processo.
        :type dict_processo: dict
        :param campos: Campos que irão preencher a linha de resultado, por default None.
        :type campos: list
        """
        data = datetime.now().strftime("%d/%m/%Y %H:%H:%M:%S")
        data = datetime.now().strftime("%d/%m/%Y %H:%H:%M:%S")
        suite = BuiltIn().get_variable_value("${SUITE_NAME}", "")
        cenario = BuiltIn().get_variable_value("${TEST_NAME}", "")
        linha = [data, suite, cenario, resultado, tempo_execucao]
        LISTA_LINHAS_RESULTADOS.append(linha)

    def criar_linha_de_metricas(self):
        """
        Registra métricas na planilha.
        """
        try:
            metricas = BuiltIn().get_variable_value("${METRICAS}", "")
            now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            row = [
                now,
                int(metricas["sucesso"]),
                int(metricas["falha"]),
            ]
            LISTA_LINHAS_METRICAS.append(row)

        except Exception as e:
            logger(
                "Registrar métricas",
                "ERROR",
                f"Erro ao registrar métricas. Detalhes: {traceback.format_exc()}",
            )
            raise Exception(
                f"Erro ao registrar métricas na planilha. Detalhes: {traceback.format_exc()}"
            ) from e

    def atualizar_planilha(self, data, sheet_name):
        """
        Atualiza uma planilha Excel com os dados fornecidos.

        :param data: Dados a serem registrados (lista de listas).
        :param sheet_name: Nome da aba a ser atualizada.
        """
        try:
            df_existing = self.capturar_dados_da_aba(sheet_name)
            df_new = pd.DataFrame(data, columns=df_existing.columns)
            df_combined = pd.concat([df_existing, df_new], ignore_index=True)

            with pd.ExcelWriter(
                PATH_PLANILHA_RESULTADOS,
                mode="a",
                engine="openpyxl",
                if_sheet_exists="overlay",
            ) as writer:
                df_combined.to_excel(writer, sheet_name=sheet_name, index=False)

            self.planilha_obj = self.capturar_planilha_excel()

        except Exception as e:
            logger(
                "Atualizar planilha",
                "ERROR",
                f"Erro ao atualizar a aba '{sheet_name}'. Detalhes: {traceback.format_exc()}",
            )
            raise Exception(
                f"Erro ao atualizar a aba {sheet_name} da planilha. Detalhes: {traceback.format_exc()}"
            ) from e

    def capturar_planilha_excel(self):
        """
        Captura uma planilha Excel.

        :return: Objeto ExcelFile.
        """
        try:
            planilha = pd.ExcelFile(PATH_PLANILHA_RESULTADOS)
            if planilha.sheet_names:
                return planilha
            else:
                raise Exception("O arquivo Excel não contém abas válidas.")
        except Exception as e:
            logger(
                "Capturar planilha",
                "ERROR",
                f"Erro ao capturar planilha '{RELATORIO_TESTES}'. Detalhes: {traceback.format_exc()}",
            )
            raise Exception(
                f"Erro ao capturar a planilha Excel. Detalhes: {traceback.format_exc()}"
            ) from e

    def capturar_dados_da_aba(self, sheet_name):
        """
        Captura os dados de uma aba da planilha.

        :param sheet_name: Nome da aba.
        :return: DataFrame com os dados da aba.
        """
        try:
            if sheet_name not in self.planilha_obj.sheet_names:
                raise ValueError(f"A aba '{sheet_name}' não existe no arquivo Excel.")
            
            return self.planilha_obj.parse(sheet_name=sheet_name, dtype=str)
        except Exception as e:
            logger(
                "Capturar dados aba",
                "ERROR",
                f"Erro ao capturar dados da aba '{sheet_name}'. Detalhes: {traceback.format_exc()}",
            )
            raise Exception(
                f"Erro ao capturar dados da aba '{sheet_name}' da planilha. Detalhes: {traceback.format_exc()}"
            ) from e

    def registrar_dados_de_todas_as_abas_excel(self):
        """
        Registra os dados em todas as abas da planilha Excel.
        """
        try:
            self.atualizar_planilha(LISTA_LINHAS_AT_OP, ATENCAO_OPERACIONAL_SHEET_NAME)
            self.atualizar_planilha(LISTA_LINHAS_RESULTADOS, RESULTADOS_SHEET_NAME)
            self.atualizar_planilha(LISTA_LINHAS_METRICAS, METRICAS_SHEET_NAME)
        except Exception as e:
            logger(
                "Registrar dados todas as abas",
                "ERROR",
                f"Erro ao registrar dados em todas as abas. Detalhes: {traceback.format_exc()}",
            )
            raise Exception(
                f"Erro ao registrar dados de todas as abas no excel. Detalhes: {traceback.print_exc()}"
            ) from e
