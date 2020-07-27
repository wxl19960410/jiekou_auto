from lib.API import myapi
from hyrobot.common import  *
def suite_setup():
    myapi.login()
    myapi.orders_del_all()
    myapi.customer_del_all()
    myapi.medicines_del_all()
def suite_teardown():
    myapi.customer_del_all()
force_tags=['添加药品功能']
class c0307:
    def teardown(self):
        myapi.medicines_del( self.addid)
    name='添加操作 -api0307'
    def teststeps(self):
        STEP(1,'添加药品')
        r=myapi.medicines_add('青霉素',"青霉素 国字号","099877883837")
        self.addid=r.json()['id']
        CHECK_POINT('ret的值',r.json()["ret"]==0)
        STEP(2,'检查操作')
        res=myapi.medicines_list().json()
        expected = {
                            "ret": 0,
                            "retlist": [
                                {"id":self.addid, "name": "青霉素", "sn": "099877883837", "desc": "青霉素 国字号"},
                                ] ,
                            'total': 1
                        }
        CHECK_POINT('返回消息体内容', expected==res)
class c0308:
    name='添加操作 -api0308'
    def teststeps(self):
        STEP(1, '添加药品')
        r = myapi.medicines_add("青霉素 国字号","099877883837")
        STEP(2, '检查操作')
        CHECK_POINT('返回消息体内容',r.json()==
                                {
                        "ret": 1,
                        "msg":  "请求消息参数错误",
                                })

class c0309:
    name = '添加操作 -api0309'
    def teststeps(self):
        STEP(1, '添加药品')
        r = myapi.medicines_add('青霉素', "青霉素 国字号")
        STEP(2, '检查操作')
        CHECK_POINT('返回消息体内容', r.json() ==
                    {
                        "ret": 1,
                        "msg": "请求消息参数错误",
                    })
class c0310:
    name='添加操作 -api0310'
    def teststeps(self):
        STEP(1, '添加药品')
        r = myapi.medicines_add('青霉素',"099877883837")
        STEP(2, '检查操作')
        CHECK_POINT('返回消息体内容', r.json() ==
                    {
                        "ret": 1,
                        "msg": "请求消息参数错误",
                    })