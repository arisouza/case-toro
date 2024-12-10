*** Settings ***
Documentation    Keywords reutilizáveis para cenários em BDD.
Resource    ${ROOT}/resources/main.resource


*** Keywords ***
Dado Que ${keyword}
    [Documentation]    Base para início das keywords com "Dado...".
    ...                Recebe como argumento o nome da keyword que deve ser acionada.
    Run Keyword    ${keyword}

Quando ${keyword}
    [Documentation]    Base para início das keywords com "Dado...".
    ...                Recebe como argumento o nome da keyword que deve ser acionada.
    Run Keyword    ${keyword}

Então ${keyword}
    [Documentation]    Base para início das keywords com "Dado...".
    ...                Recebe como argumento o nome da keyword que deve ser acionada.
    Run Keyword    ${keyword}

E ${keyword}
    [Documentation]    Base para início das keywords com "Dado...".
    ...                Recebe como argumento o nome da keyword que deve ser acionada.
    Run Keyword    ${keyword}
