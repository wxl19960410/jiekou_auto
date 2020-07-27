*** Settings ***

Library  客户操作3个客户.py   WITH NAME  F

Suite Setup    F.suite_setup

Force Tags     列出用户功能  

Library  客户操作3个客户.c0206   WITH NAME  c0206



*** Test Cases ***

列出 api-0206

  c0206.teststeps
