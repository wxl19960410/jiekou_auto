*** Settings ***

Library  删除操作有用户.py   WITH NAME  F

Suite Setup    F.suite_setup

Suite Teardown    F.suite_teardown

Force Tags     删除用户功能  

Library  删除操作有用户.c0223   WITH NAME  c0223



*** Test Cases ***

删除用户 -api0223

  c0223.teststeps
