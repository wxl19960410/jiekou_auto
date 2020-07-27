*** Settings ***

Library  列出订单无订单.py   WITH NAME  F

Suite Setup    F.suite_setup

Force Tags     列出订单功能  

Library  列出订单无订单.c0401   WITH NAME  c0401

Library  列出订单无订单.c0402   WITH NAME  c0402

Library  列出订单无订单.c0403   WITH NAME  c0403

Library  列出订单无订单.c0404   WITH NAME  c0404



*** Test Cases ***

列出 api-0401

  c0401.teststeps


列出 api-0402

  c0402.teststeps


列出 api-0403

  c0403.teststeps


列出 api-0404

  c0404.teststeps
