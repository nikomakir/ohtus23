*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  testi
    Set Password    hyvaksytty1
    Set Password Confirmation  hyvaksytty1
    Submit Credentials Register
    Register Should Succeed
    
Register With Too Short Username And Valid Password
    Set Username    a
    Set Password    hyvaksytty1
    Set Password Confirmation    hyvaksytty1
    Submit Credentials Register
    Register Should Fail With Message    Username must consist of letters a-z and be at least 3 characters long


Register With Valid Username And Invalid Password
    Set Username    testi
    Set Password    aaa
    Set Password Confirmation    aaa
    Submit Credentials Register
    Register Should Fail With Message    Password must be at least 8 characters long and contain special characters or numbers

Register With Nonmatching Password And Password Confirmation
    Set Username    testi
    Set Password    hyvaksytty1
    Set Password Confirmation    ei
    Submit Credentials Register
    Register Should Fail With Message    Passwords do not match

Login After Successful Registration
    Set Username    toinen
    Set Password    hyvaksytty1
    Set Password Confirmation    hyvaksytty1
    Submit Credentials Register
    Click Link    Continue to main page
    Click Button    Logout
    Set Username    toinen
    Set Password    hyvaksytty1
    Submit Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username    a
    Set Password    hyvaksytty1
    Set Password Confirmation    hyvaksytty1
    Submit Credentials Register
    Click Link    Login
    Set Username    a
    Set Password    hyvaksytty1
    Submit Credentials
    Login Should Fail With Message    Invalid username or password


*** Keywords ***

Submit Credentials
    Click Button  Login

Submit Credentials Register
    Click Button  Register

Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain    ${message}

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password    password_confirmation    ${password}