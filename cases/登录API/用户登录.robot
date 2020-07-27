*** Settings ***

Library  用户登录.py   WITH NAME  F

Suite Setup    F.suite_setup

Force Tags     登录功能  

Library  用户登录.C_login_pass   WITH NAME  C_login_pass

Library  用户登录.C_login_fail   WITH NAME  C_login_fail



*** Test Cases ***

登录 api-0101

  C_login_pass.teststeps


登录 api-0102

  C_login_fail.teststeps   ${0}


登录 api-0103

  C_login_fail.teststeps   ${1}


登录 api-0104

  C_login_fail.teststeps   ${2}


登录 api-0105

  C_login_fail.teststeps   ${3}


登录 api-0106

  C_login_fail.teststeps   ${4}
