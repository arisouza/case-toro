*** Settings ***
Documentation    Keywords de setup e teardown.
Resource    ${ROOT}/resources/main.resource


*** Keywords ***
Inicializando Os Testes
    [Documentation]    Abre o navegador Chrome na URL recebida como argumento.
    [Arguments]    ${URL}
    Open Browser    ${URL}    Chrome
    Log    Browser aberto em ${URL}    console=True
    ${METRICAS}    Create Dictionary    sucesso=${0}    falha=${0}
    Set Global Variable    ${METRICAS}

Setup Teste
    [Documentation]    Define o horário de início do teste.
    ${horario_inicio_teste}    Get Current Date
    Set Suite Variable    ${HORARIO_INICIO_TESTE}

Teardown Teste
    [Documentation]    Define o tempo de execução do teste e registra o resultado.
    ${horario_fim_teste}    Get Current Date
    Set Suite Variable    ${HORARIO_FIM_TESTE}
    ${tempo_execucao}    Subtract Date From Date    ${HORARIO_FIM_TESTE}    ${HORARIO_INICIO_TESTE}
    ...    result_format=timer
    Set Suite Variable    ${TEMPO_EXECUCAO}
    IF    '${TEST_STATUS}' == 'FAIL'
        Criar Linha De Resultado    FALHA    ${tempo_execucao}
        Criar Linha De Detalhes Da Falha    ${TEST_MESSAGE}
        ${falhas}    Evaluate    ${METRICAS}[falha] + 1
        Set To Dictionary    ${METRICAS}    falha=${falhas}
    ELSE
        ${sucessos}    Evaluate    ${METRICAS}[sucesso] + 1
        Set To Dictionary    ${METRICAS}    sucesso=${sucessos}
        Criar Linha De Resultado    SUCESSO    ${tempo_execucao}
    END
