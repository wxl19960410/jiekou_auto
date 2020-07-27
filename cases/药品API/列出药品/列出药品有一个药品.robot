*** Settings ***

Library  列出药品有一个药品.py   WITH NAME  F

Suite Setup    F.suite_setup

Force Tags     列出药品功能  

Library  列出药品有一个药品.c0305   WITH NAME  c0305



*** Test Cases ***

列出 api-0305

  c0305.teststeps
