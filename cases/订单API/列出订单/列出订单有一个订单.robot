*** Settings ***

Library  列出订单有一个订单.py   WITH NAME  F

Suite Setup    F.suite_setup

Force Tags     列出订单功能  

Library  列出订单有一个订单.c0405   WITH NAME  c0405

Library  列出订单有一个订单.c0406   WITH NAME  c0406



*** Test Cases ***

列出 api-0405
  [Setup]     c0405.setup

  c0405.teststeps


列出 api-0406
  [Setup]     c0406.setup

  c0406.teststeps
