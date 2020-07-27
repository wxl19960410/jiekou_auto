*** Settings ***

Library  客户操作 空白.py   WITH NAME  F

Suite Setup    F.suite_setup

Force Tags     列出用户功能  

Library  客户操作 空白.c0201   WITH NAME  c0201

Library  客户操作 空白.c0202   WITH NAME  c0202

Library  客户操作 空白.c0203   WITH NAME  c0203

Library  客户操作 空白.c0204   WITH NAME  c0204



*** Test Cases ***

列出 api-0201

  c0201.teststeps


列出 api-0202

  c0202.teststeps


列出 api-0203

  c0203.teststeps


列出 api-0204

  c0204.teststeps
