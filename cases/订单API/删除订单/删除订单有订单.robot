*** Settings ***

Library  删除订单有订单.py   WITH NAME  F

Suite Setup    F.suite_setup

Suite Teardown    F.suite_teardown

Force Tags     删除订单功能  

Library  删除订单有订单.c0409   WITH NAME  c0409



*** Test Cases ***

删除订单 -api0409
  [Setup]     c0409.setup

  c0409.teststeps
