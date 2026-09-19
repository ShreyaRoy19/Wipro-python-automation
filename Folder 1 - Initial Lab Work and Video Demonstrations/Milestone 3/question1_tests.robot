*** Settings ***
Library           SeleniumLibrary

*** Variables ***
${URL}            https://the-internet.herokuapp.com/login
${USERNAME}       ShreyaRoy

*** Test Cases ***
1. Open Browser And Fill Form Field Test
    Open Browser    ${URL}    chrome
    Maximize Browser Window
    Input Text    id=username    ${USERNAME}
    Close Browser

2. Verify Element Presence Test
    Open Browser    ${URL}    chrome
    Maximize Browser Window
    Page Should Contain Element    css=button[type='submit']
    Close Browser