*** Settings ***
Documentation    Arquivo que armazena os locators da página de login.


*** Variables ***
${URL_LOGIN}    https://app.toroinvestimentos.com.br/entrar
${H3_LOGIN}     Acesse sua conta Toro.

&{INPUT}    email_cpf= id:username
...         senha= id:password

&{BUTTON}    entrar= xpath://button/span[text()="Entrar"]
