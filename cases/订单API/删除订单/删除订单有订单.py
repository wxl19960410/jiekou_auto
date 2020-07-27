from lib.API import myapi
from hyrobot.common import  *
def suite_setup():
    myapi.login()
    myapi.orders_del_all()
    myapi.customer_del_all()
    myapi.medicines_del_all()
def suite_teardown():
    myapi.orders_del_all()
force_tags=['删除订单功能']
class c0409:
    name='删除订单 -api0409'
    def setup(self):
        myapi.customer_add('华山医院订单002', '15951813663', '南京市鼓楼区')
        addcid = myapi.customer_list().json()["retlist"][0]["id"]
        myapi.medicines_add("青霉素", "青霉素 国字号", "234324234234")
        addmid = myapi.medicines_list().json()["retlist"][0]["id"]
        myapi.orders_add("华山医院订单002", addcid, [
            {"id": addmid, "amount": 3, "name": "青霉素"}])
    def teststeps(self):
        STEP(1,'删除操作')
        r=myapi.orders_list().json()
        addid = r["retlist"][0]["id"]
        res=myapi.orders_del(addid)
        STEP(2,'检查操作')
        CHECK_POINT('检查消息体内容',res.json()=={"ret": 0, "id": addid})
