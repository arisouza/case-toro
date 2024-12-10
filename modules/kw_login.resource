*** Settings ***
Documentation    Keywords relacionadas à página de login.
Resource    ${ROOT}/resources/main.resource


*** Keywords ***
O Usuário Preenche O Campo "E-mail" Com "${email}"
    [Documentation]    Insere o e-mail recebido como argumento no campo de e-mail.
    Wait Until Element Is Visible    ${INPUT.email_cpf}
    Input Text    ${INPUT.email_cpf}    ${email}
    Log    E-mail inserido: ${email}    console=True

Preenche O Campo "Senha" Com "${senha}"
    [Documentation]    Insere a senha recebida como argumento no campo senha.
    Wait Until Element Is Visible    ${INPUT.senha}
    Input Password    ${INPUT.senha}    ${senha}
    Log    Senha inserida.    console=True

Clica No Botão "Entrar"
    [Documentation]    Realiza o click no botão entrar.
    Wait Until Element Is Visible    ${BUTTON.entrar}
    Click Element    ${BUTTON.entrar}
    Log    Click realizado sobre o botão "Entrar".    console=True

O Usuário Deve Ser Redirecionado Para A Página Principal
    [Documentation]    Valida se o usuário está na página principal.
    Wait Until Page Contains    ${H3}
