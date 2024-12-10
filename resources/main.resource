*** Settings ***
Documentation    Arquivo de recursos utilizados.

# Bibliotecas Robot
Library    DateTime
Library    Collections
Library    RPA.Browser.Selenium

# Bibliotecas Customizadas
Library     ${ROOT}/libraries/RelatorioProdutividade.py

# Keywords
Resource    ${ROOT}/modules/bdd.resource
Resource    ${ROOT}/modules/kw_login.resource
Resource    ${ROOT}/modules/kw_common.resource
Resource    ${ROOT}/modules/setup_teardown.resource

# Locators
Resource    ${ROOT}/resources/locators_login.resource
Resource    ${ROOT}/resources/locators_principal.resource
