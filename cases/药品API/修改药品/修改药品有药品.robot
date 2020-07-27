*** Settings ***

Library  修改药品有药品.py   WITH NAME  F

Suite Setup    F.suite_setup

Suite Teardown    F.suite_teardown

Force Tags     修改药品功能  

Library  修改药品有药品.c0314   WITH NAME  c0314

Library  修改药品有药品.c0315   WITH NAME  c0315

Library  修改药品有药品.c0316   WITH NAME  c0316

Library  修改药品有药品.c0317   WITH NAME  c0317

Library  修改药品有药品.c0318   WITH NAME  c0318

Library  修改药品有药品.c0319   WITH NAME  c0319

Library  修改药品有药品.c0320   WITH NAME  c0320

Library  修改药品有药品.c0321   WITH NAME  c0321



*** Test Cases ***

修改药品 -api0314
  [Teardown]  c0314.teardown

  c0314.teststeps


修改药品 -api0315
  [Teardown]  c0315.teardown

  c0315.teststeps


修改药品 -api0316
  [Teardown]  c0316.teardown

  c0316.teststeps


修改药品 -api0317
  [Teardown]  c0317.teardown

  c0317.teststeps


修改药品 -api0318
  [Teardown]  c0318.teardown

  c0318.teststeps


修改药品 -api0319
  [Teardown]  c0319.teardown

  c0319.teststeps


修改药品 -api0320
  [Teardown]  c0320.teardown

  c0320.teststeps


修改药品 -api0321

  c0321.teststeps
