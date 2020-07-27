*** Settings ***

Library  删除用户空.py   WITH NAME  F

Suite Setup    F.suite_setup

Force Tags     删除用户功能  

Library  删除用户空.c0222   WITH NAME  c0222



*** Test Cases ***

删除用户 -api0222

  c0222.teststeps
