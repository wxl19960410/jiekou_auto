*** Settings ***

Library  修改操作有用户.py   WITH NAME  F

Suite Setup    F.suite_setup

Suite Teardown    F.suite_teardown

Force Tags     修改用户功能  

Library  修改操作有用户.c0214   WITH NAME  c0214

Library  修改操作有用户.c0215   WITH NAME  c0215

Library  修改操作有用户.c0216   WITH NAME  c0216

Library  修改操作有用户.c0217   WITH NAME  c0217

Library  修改操作有用户.c0218   WITH NAME  c0218

Library  修改操作有用户.c0219   WITH NAME  c0219

Library  修改操作有用户.c0220   WITH NAME  c0220

Library  修改操作有用户.c0221   WITH NAME  c0221



*** Test Cases ***

修改用户 -api0214
  [Teardown]  c0214.teardown

  c0214.teststeps


修改用户 -api0215
  [Teardown]  c0215.teardown

  c0215.teststeps


修改用户 -api0216
  [Teardown]  c0216.teardown

  c0216.teststeps


修改用户 -api0217
  [Teardown]  c0217.teardown

  c0217.teststeps


修改用户 -api0218
  [Teardown]  c0218.teardown

  c0218.teststeps


修改用户 -api0219
  [Teardown]  c0219.teardown

  c0219.teststeps


修改用户 -api0220
  [Teardown]  c0220.teardown

  c0220.teststeps


修改用户 -api0221

  c0221.teststeps
