from lib.API import myapi
from hyrobot.common import  *

def suite_setup():
    myapi.login()
    myapi.orders_del_all()
    myapi.customer_del_all()
    myapi.medicines_del_all()


force_tags=['列出药品功能']
class c0301:
    name='列出 api-0301'
    def teststeps(self):
        STEP(1,'列出操作')
        response=myapi.medicines_list()
        STEP(2,'检查操作')
        CHECK_POINT('检查返回消息体',response.json()==
                    {
                    "ret": 0,
                    "retlist":[],
                    'total': 0
                    })
class c0302:
    name='列出 api-0302'
    def teststeps(self):
        STEP(1,'列出操作')
        response=myapi.medicines_list(None,1,'')
        STEP(2,'检查操作')
        CHECK_POINT('检查返回消息体', response.json()["ret"]!=0)

class c0303:
    name='列出 api-0303'
    def teststeps(self):
        STEP(1,'列出操作')
        response=myapi.medicines_list(10,None,'')
        STEP(2,'检查操作')
        CHECK_POINT('检查返回消息体', response.json()["ret"]!=0)
class c0304:
    name='列出 api-0304'
    def teststeps(self):
        STEP(1,'列出操作')
        response=myapi.medicines_list(10,1,None)
        STEP(2,'检查操作')
        CHECK_POINT('检查返回消息体',response.json() =={
                                                            "ret": 0,
                                                            "retlist":[],
                                                            'total': 0
                                                            })