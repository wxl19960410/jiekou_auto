from lib.API import myapi
from hyrobot.common import  *
def suite_setup():
    myapi.login()
    myapi.orders_del_all()
    myapi.customer_del_all()
    myapi.medicines_del_all()
    myapi.medicines_add( "青霉素","青霉素 国字号","234324234234")
def suite_teardown():
    myapi.medicines_del_all()

force_tags=['添加药品功能']

class c0311:
    name='添加药品 -api0311'
    def teststeps(self):
        STEP(1,'添加药品')
        r=myapi.medicines_add( "青霉素1","青霉素 国字号","234324234234")
        CHECK_POINT('ret的值', r.json()["ret"] == 0)
        STEP(2, '检查操作')
        res = myapi.medicines_list().json()
        CHECK_POINT('响应消息体内容ret', res["ret"] ==0)
        CHECK_POINT('响应消息体内容total',res["total"]==2)
class c0312:
    name = '添加药品 -api0312'
    def teststeps(self):
        STEP(1, '添加药品')
        r = myapi.medicines_add( "青霉素","青霉素 国字号","234324234234")
        STEP(2, '检查操作')
        CHECK_POINT('消息体内容',r.json()["ret"]!=0)
