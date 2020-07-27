*** Settings ***

Library  添加药品有药品.py   WITH NAME  F

Suite Setup    F.suite_setup

Suite Teardown    F.suite_teardown

Force Tags     添加药品功能  

Library  添加药品有药品.c0311   WITH NAME  c0311

Library  添加药品有药品.c0312   WITH NAME  c0312



*** Test Cases ***

添加药品 -api0311

  c0311.teststeps


添加药品 -api0312

  c0312.teststeps
