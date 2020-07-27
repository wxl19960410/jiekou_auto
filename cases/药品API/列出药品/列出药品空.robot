*** Settings ***

Library  列出药品空.py   WITH NAME  F

Suite Setup    F.suite_setup

Force Tags     列出药品功能  

Library  列出药品空.c0301   WITH NAME  c0301

Library  列出药品空.c0302   WITH NAME  c0302

Library  列出药品空.c0303   WITH NAME  c0303

Library  列出药品空.c0304   WITH NAME  c0304



*** Test Cases ***

列出 api-0301

  c0301.teststeps


列出 api-0302

  c0302.teststeps


列出 api-0303

  c0303.teststeps


列出 api-0304

  c0304.teststeps
