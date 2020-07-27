from lib.API import myapi
from hyrobot.common import  *
def suite_setup():
    myapi.login()
    myapi.orders_del_all()
    myapi.customer_del_all()
    myapi.medicines_del_all()
force_tags=['修改用户功能']
class c0213:
    name='修改用户 -api0213'
    def teststeps(self):
        STEP(1,'修改操作')
        r=myapi.customer_alter(45,'wxl',123456,'nanjingyoudian')
        STEP(2,'检查操作')
        CHECK_POINT('检查消息体内容',r.json()==
                             {
                                 "ret": 1,
                                 "msg": "客户ID不存在"})