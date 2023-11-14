*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Keywords ***
Input New Command And Create User
    Create User  kalle  kalle123
    Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials    joku    testisalasana123
    Output Should Contain    New user registered

Register With Already Taken Username And Valid Password
    Input Credentials    kalle    jotain123
    Output Should Contain    User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials    a    jotain123
    Output Should Contain    Username must be longer than 3 characters


Register With Enough Long But Invalid Username And Valid Password
    Input Credentials    joku123    jotain123
    Output Should Contain    Username must consist of letters a-z

Register With Valid Username And Too Short Password
    Input Credentials    joku    a
    Output Should Contain    Password must be longer than 8 characters

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials    joku    jotainkahdeksan
    Output Should Contain    Password must contain numbers or special characters

