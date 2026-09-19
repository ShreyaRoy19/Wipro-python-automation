*** Settings ***
Library           SeleniumLibrary
Library           OperatingSystem
Library           String
Library           Collections

*** Variables ***
${URL}            https://the-internet.herokuapp.com/login
${VALID_USER}     tomsmith
${VALID_PASS}     SuperSecretPassword!

*** Test Cases ***
1. Variable Implementation Test
    [Documentation]    Test case using internal variables for authentication data
    Open Browser    ${URL}    chrome
    Maximize Browser Window
    Input Text    id=username    ${VALID_USER}
    Input Text    id=password    ${VALID_PASS}
    Click Button    css=button[type='submit']
    Page Should Contain Element    id=flash
    Close Browser

2. External File Data-Driven Test
    [Documentation]    Test case reading and iterating data safely from testdata.csv
    ${file_content}=    Get File    testdata.csv
    @{lines}=    Split To Lines    ${file_content}
    Remove From List    ${lines}    0
    FOR    ${line}    IN    @{lines}
        ${clean_line}=    Strip String    ${line}
        Run Keyword If    '${clean_line}' != ''    Process CSV Row    ${clean_line}
    END

*** Keywords ***
Process CSV Row
    [Arguments]    ${row_string}
    @{words}=    Split String    ${row_string}    ,
    ${user}=    Strip String    ${words[0]}
    ${pass}=    Strip String    ${words[1]}
    Execute Login Attempt    ${user}    ${pass}

Execute Login Attempt
    [Arguments]    ${user}    ${pass}
    Open Browser    ${URL}    chrome
    Maximize Browser Window
    Input Text    id=username    ${user}
    Input Text    id=password    ${pass}
    Click Button    css=button[type='submit']
    Page Should Contain Element    id=flash
    Close Browser