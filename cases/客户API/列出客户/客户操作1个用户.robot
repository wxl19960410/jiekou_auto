*** Settings ***

Library  客户操作1个用户.py   WITH NAME  F

Suite Setup    F.suite_setup

Force Tags     列出用户功能  

Library  客户操作1个用户.c0205   WITH NAME  c0205



*** Test Cases ***

列出 api-0205

  c0205.teststeps
