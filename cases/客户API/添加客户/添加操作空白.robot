*** Settings ***

Library  添加操作空白.py   WITH NAME  F

Suite Setup    F.suite_setup

Suite Teardown    F.suite_teardown

Force Tags     添加用户功能  

Library  添加操作空白.c0207   WITH NAME  c0207

Library  添加操作空白.c0208   WITH NAME  c0208

Library  添加操作空白.c0209   WITH NAME  c0209

Library  添加操作空白.c0210   WITH NAME  c0210



*** Test Cases ***

添加操作 -api0207
  [Teardown]  c0207.teardown

  c0207.teststeps


添加操作 -api0208

  c0208.teststeps


添加操作 -api0209

  c0209.teststeps


添加操作 -api0210

  c0210.teststeps
