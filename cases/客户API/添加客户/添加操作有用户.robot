*** Settings ***

Library  添加操作有用户.py   WITH NAME  F

Suite Setup    F.suite_setup

Suite Teardown    F.suite_teardown

Force Tags     添加用户功能  

Library  添加操作有用户.c0211   WITH NAME  c0211

Library  添加操作有用户.c0212   WITH NAME  c0212



*** Test Cases ***

添加客户 -api0211

  c0211.teststeps


添加客户 -api0212

  c0212.teststeps
