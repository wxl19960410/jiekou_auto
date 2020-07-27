from lib.API import myapi
from hyrobot.common import  *
def suite_setup():
    myapi.login()
    myapi.orders_del_all()
    myapi.customer_del_all()
    myapi.medicines_del_all()
force_tags=['删除用户功能']
class c0222:
    name='删除用户 -api0222'
    def teststeps(self):
        STEP(1,'删除操作')
        r=myapi.customer_del(48)
        STEP(2,'检查操作')
        CHECK_POINT('检查消息体内容',r.json()["ret"]!=0)
