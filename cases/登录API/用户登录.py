from hyrobot.common import *
from lib.API import myapi
def suite_setup():
    myapi.login()
    myapi.customer_del_all()
    myapi.medicines_del_all()
    myapi.orders_del_all()
def suite_teardowm():
    pass
force_tags=['登录功能']

class C_login_pass:
    name = '登录 api-0101'
    def teststeps(self):
        STEP(1, '登录操作')
        response = myapi.login('byhy', '88888888')
        STEP(2, '检查操作')
        CHECK_POINT('查看ret的值是否为0', response.json()["ret"] == 0)

class C_login_fail:
    cases=[
        ('登录 api-0102','','88888888'),
        ('登录 api-0103','byhy',''),
        ('登录 api-0104', 'byh', '88888888'),
        ('登录 api-0105', 'byhy', '123456'),
        ('登录 api-0106', 'byhyb', '888888123')
    ]
    def teststeps(self,para_index):
        STEP(1, '登录操作')
        username,password=self.cases[para_index][1:]
        response=myapi.login(username=username,password=password)
        STEP(2, '检查操作')
        CHECK_POINT('查看ret的值是否为1', response.json()['ret'] == 1)
        CHECK_POINT('查看返回消息体内容', response.json() ==
                    {
                        "ret": 1,
                        "msg":  "用户名或者密码错误" })

















