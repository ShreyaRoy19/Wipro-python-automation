*** Settings ***
Library           SeleniumLibrary

*** Variables ***
${URL}            https://the-internet.herokuapp.com/login
${STUDENT_USER}   ShreyaRoy
${VALID_PASS}     SuperSecretPassword!

*** Test Cases ***
3. Custom Keywords Implementation Test
    [Documentation]    Test case executing modular custom keywords with arguments
    Open Login Page And Maximize    ${URL}
    Fill Login Form And Submit    ${STUDENT_USER}    ${VALID_PASS}
    Verify Flash Banner Presence
    Close Browser

*** Keywords ***
Open Login Page And Maximize
    [Arguments]    ${target_url}
    Open Browser    ${target_url}    chrome
    Maximize Browser Window

Fill Login Form And Submit
    [Arguments]    ${username}    ${password}
    Input Text    id=username    ${username}
    Input Text    id=password    ${password}
    Click Button    css=button[type='submit']

Verify Flash Banner Presence
    Page Should Contain Element    id=flash