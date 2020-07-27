*** Settings ***

Library  添加药品空白.py   WITH NAME  F

Suite Setup    F.suite_setup

Suite Teardown    F.suite_teardown

Force Tags     添加药品功能  

Library  添加药品空白.c0307   WITH NAME  c0307

Library  添加药品空白.c0308   WITH NAME  c0308

Library  添加药品空白.c0309   WITH NAME  c0309

Library  添加药品空白.c0310   WITH NAME  c0310



*** Test Cases ***

添加操作 -api0307
  [Teardown]  c0307.teardown

  c0307.teststeps


添加操作 -api0308

  c0308.teststeps


添加操作 -api0309

  c0309.teststeps


添加操作 -api0310

  c0310.teststeps
