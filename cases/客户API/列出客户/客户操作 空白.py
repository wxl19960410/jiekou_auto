from lib.API import myapi
from hyrobot.common import  *

def suite_setup():
    myapi.login()
    myapi.orders_del_all()
    myapi.customer_del_all()
    myapi.medicines_del_all()

def suite_teardowm():
    pass

force_tags=['列出用户功能']
class c0201:
    name='列出 api-0201'
    def teststeps(self):
        STEP(1,'列出操作')
        response=myapi.customer_list()
        STEP(2,'检查操作')
        CHECK_POINT('检查返回消息体',response.json()==
                    {
                    "ret": 0,
                    "retlist":[],
                    'total': 0
                    })
class c0202:
    name='列出 api-0202'
    def teststeps(self):
        STEP(1,'列出操作')
        response=myapi.customer_list(None,1,'')
        STEP(2,'检查操作')
        CHECK_POINT('检查返回消息体', response.json()["ret"]!=0)

class c0203:
    name='列出 api-0203'
    def teststeps(self):
        STEP(1,'列出操作')
        response=myapi.customer_list(10,None,'')
        STEP(2,'检查操作')
        CHECK_POINT('检查返回消息体', response.json()["ret"]!=0)
class c0204:
    name='列出 api-0204'
    def teststeps(self):
        STEP(1,'列出操作')
        response=myapi.customer_list(10,1,None)
        STEP(2,'检查操作')
        CHECK_POINT('检查返回消息体', response.json()=={
                                                    "ret": 0,
                                                    "retlist":[],
                                                    'total': 0
                                                    })