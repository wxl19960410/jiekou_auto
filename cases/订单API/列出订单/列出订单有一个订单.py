from lib.API import myapi
from hyrobot.common import  *

def suite_setup():
    myapi.login()
    myapi.orders_del_all()
    myapi.customer_del_all()
    myapi.medicines_del_all()

def suite_teardowm():
    myapi.orders_del_all()

force_tags=['列出订单功能']
class c0405:
    name='列出 api-0405'
    def setup(self):
        myapi.orders_add("华山医院订单002", "3", [
            {"id": 16, "amount": 5, "name": "环丙沙星"},
            {"id": 15, "amount": 5, "name": "克林霉素"}])
    def teststeps(self):
        STEP(1,'列出操作')
        response=myapi.orders_list()
        STEP(2,'检查操作')
        CHECK_POINT('检查返回消息体ret',response.json()["ret"]==0)
        CHECK_POINT('检查返回消息体total', response.json()["total"] == 0)
class c0406:
    name='列出 api-0406'
    def setup(self):
         myapi.customer_add('华山医院订单002','15951813663','南京市鼓楼区')
         addcid=myapi.customer_list().json()["retlist"][0]["id"]
         myapi.medicines_add("青霉素","青霉素 国字号","234324234234")
         addmid=myapi.medicines_list().json()["retlist"][0]["id"]
         myapi.orders_add("华山医院订单002", addcid, [
            {"id": addmid, "amount": 3, "name": "青霉素"}])
    def teststeps(self):
        STEP(1, '列出操作')
        response = myapi.orders_list()
        STEP(2, '检查操作')
        CHECK_POINT('检查返回消息体ret', response.json()["ret"] == 0)
        CHECK_POINT('检查返回消息体total', response.json()["total"] == 1)


