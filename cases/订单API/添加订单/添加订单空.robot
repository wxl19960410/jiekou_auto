*** Settings ***

Library  添加订单空.py   WITH NAME  F

Suite Setup    F.suite_setup

Suite Teardown    F.suite_teardown

Force Tags     列出订单功能  

Library  添加订单空.c0407   WITH NAME  c0407



*** Test Cases ***

列出 api-0407
  [Setup]     c0407.setup

  c0407.teststeps
