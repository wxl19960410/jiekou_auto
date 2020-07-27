from lib.API import myapi
from hyrobot.common import  *
def suite_setup():
    myapi.login()
    myapi.orders_del_all()
    myapi.customer_del_all()
    myapi.medicines_del_all()
    myapi.customer_add("武汉市桥西医院", "13345679934", "武汉市桥西医院北路")
def suite_teardown():
    myapi.customer_del_all()

force_tags=['添加用户功能']
class c0211:
    name='添加客户 -api0211'
    def teststeps(self):
        STEP(1,'添加用户')
        r=myapi.customer_add("wxl", "133456799345", "nanjingyoudian")
        CHECK_POINT('ret的值', r.json()["ret"] == 0)
        STEP(2, '检查操作')
        res = myapi.customer_list().json()
        CHECK_POINT('响应消息体内容ret', res["ret"] ==0)
        CHECK_POINT('响应消息体内容total',res["total"]==2)
class c0212:
    name = '添加客户 -api0212'
    def teststeps(self):
        STEP(1, '添加用户')
        r = myapi.customer_add("武汉市桥西医院", "13345679934", "武汉市桥西医院北路")
        STEP(2, '检查操作')
        CHECK_POINT('消息体内容',r.json()==
                    {
                        "ret": 1,
                        "msg": "客户名已经存在"
                    })





