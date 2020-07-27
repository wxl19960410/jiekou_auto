*** Settings ***

Library  删除药品空白.py   WITH NAME  F

Suite Setup    F.suite_setup

Force Tags     删除药品功能  

Library  删除药品空白.c0322   WITH NAME  c0322



*** Test Cases ***

删除药品 -api0322

  c0322.teststeps
