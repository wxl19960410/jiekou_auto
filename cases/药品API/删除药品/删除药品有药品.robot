*** Settings ***

Library  删除药品有药品.py   WITH NAME  F

Suite Setup    F.suite_setup

Suite Teardown    F.suite_teardown

Force Tags     删除药品功能  

Library  删除药品有药品.c0323   WITH NAME  c0323



*** Test Cases ***

删除药品 -api0323

  c0323.teststeps
