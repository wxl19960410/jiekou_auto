from lib.API import myapi
from hyrobot.common import  *
def suite_setup():
    myapi.login()
    myapi.orders_del_all()
    myapi.customer_del_all()
    myapi.medicines_del_all()
force_tags=['删除药品功能']
class c0322:
    name='删除药品 -api0322'
    def teststeps(self):
        STEP(1,'删除操作')
        r=myapi.medicines_del(50)
        STEP(2,'检查操作')
        CHECK_POINT('检查消息体内容',r.json()["ret"]!=0)