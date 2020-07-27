*** Settings ***

Library  删除订单空白.py   WITH NAME  F

Suite Setup    F.suite_setup

Force Tags     删除订单功能  

Library  删除订单空白.c0408   WITH NAME  c0408



*** Test Cases ***

删除订单 -api0408

  c0408.teststeps
