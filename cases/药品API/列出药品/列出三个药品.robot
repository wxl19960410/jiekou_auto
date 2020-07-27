*** Settings ***

Library  列出三个药品.py   WITH NAME  F

Suite Setup    F.suite_setup

Force Tags     列出药品功能  

Library  列出三个药品.c0306   WITH NAME  c0306



*** Test Cases ***

列出 api-0306

  c0306.teststeps
