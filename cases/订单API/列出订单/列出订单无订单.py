from lib.API import myapi
from hyrobot.common import  *
import allure

def suite_setup():
    myapi.login()
    myapi.orders_del_all()
    myapi.customer_del_all()
    myapi.medicines_del_all()


force_tags=['列出订单功能']
@allure.feature('列出订单无订单')
@allure.story('api-0401')
class c0401:
    name='列出 api-0401'
    def teststeps(self):
        STEP(1,'列出操作')
        response=myapi.orders_list()
        STEP(2,'检查操作')
        CHECK_POINT('检查返回消息体',response.json()==
                    {
                    "ret": 0,
                    "retlist":[],
                    'total': 0
                    })
@allure.feature('列出订单无订单')
@allure.story('api-0402')
class c0402:
    name='列出 api-0402'
    def teststeps(self):
        STEP(1,'列出操作')
        response=myapi.medicines_list(None,1,'')
        STEP(2,'检查操作')
        CHECK_POINT('检查返回消息体', response.json()["ret"]!=0)
@allure.feature('列出订单无订单')
@allure.story('api-0403')
@allure.severity('critical')
class c0403:
    name='列出 api-0403'
    def teststeps(self):
        STEP(1,'列出操作')
        response=myapi.orders_list(10,None,'')
        STEP(2,'检查操作')
        CHECK_POINT('检查返回消息体', response.json()["ret"]!=0)
@allure.feature('列出订单无订单')
@allure.story('api-0404')
class c0404:
    name='列出 api-0404'
    def teststeps(self):
        STEP(1,'列出操作')
        response=myapi.orders_list(10,1,None)
        STEP(2,'检查操作')
        CHECK_POINT('检查返回消息体',response.json() =={
                                                            "ret": 0,
                                                            "retlist":[],
                                                            'total': 0
                                                            })