*** Settings ***
Documentation    Keywords genéricas que podem ser usadas em diversas páginas.
Resource    ${ROOT}/resources/main.resource


*** Keywords ***
O Usuário Está Na Página: ${nome_pagina}
    [Documentation]    Direciona o browser para a página recebida como argumento e aguarda até que o H3 correspondente
    ...                à página aparecer na página.
    ...                **OBS: O nome da página passado como argumento deve ter uma variável H3_{nome_pagina}.
    Wait Until Page Contains    ${H3_${nome_pagina.upper()}}
    Log    Página ${nome_pagina} acessada com ${H3_${nome_pagina}} visível.    console=True
