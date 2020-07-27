from lib.API import myapi
from hyrobot.common import  *
def suite_setup():
    myapi.login()
    myapi.orders_del_all()
    myapi.customer_del_all()
    myapi.medicines_del_all()
force_tags=['修改药品功能']
class c0313:
    name='修改药品 -api0313'
    def teststeps(self):
        STEP(1,'修改药品')
        r=myapi.medicines_alter(45,'青霉素','青霉素 国字号','099877883837')
        STEP(2,'检查操作')
        CHECK_POINT('检查消息体内容',r.json()==
                             {
                                 "ret": 1,
                                 "msg": "药品ID不存在"})