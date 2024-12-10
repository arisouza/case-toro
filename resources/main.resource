*** Settings ***
Documentation    Arquivo de recursos utilizados.

Library    DateTime
Library    Collections
Library    RPA.Browser.Selenium
Resource    ${ROOT}/modules/bdd.resource
Resource    ${ROOT}/resources/locators_login.resource
Resource    ${ROOT}/modules/kw_login.resource
Resource    ${ROOT}/modules/kw_common.resource
Resource    ${ROOT}/resources/locators_principal.resource
Resource    ${ROOT}/modules/setup_teardown.resource
Library     ${ROOT}/libraries/RelatorioProdutividade.py
