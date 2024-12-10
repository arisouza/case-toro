*** Settings ***
Documentation     Suíte de testes para a funcionalidade de login.
Resource          ${ROOT}/resources/main.resource
Suite Setup       Inicializando Os Testes    ${URL_LOGIN}
Suite Teardown    Registrar Dados De Todas As Abas Excel
Test Setup        Setup Teste
Test Teardown     Teardown Teste


*** Test Cases ***
Login Com Credenciais Válidas
    [Documentation]    Realiza o login com credenciais válidas.
    Dado Que O Usuário Está Na Página: Login
    Quando O Usuário Preenche O Campo "E-mail" Com "${EMAIL_VALIDO}"
    E Preenche O Campo "Senha" Com "${SENHA}"
    E Clica No Botão "Entrar"
    Então O Usuário Está Na Página: Principal
    E Deve Visualizar A Mensagem Principal
