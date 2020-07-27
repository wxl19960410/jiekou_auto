from lib.API import myapi
from hyrobot.common import  *
def suite_setup():
    myapi.login()
    myapi.orders_del_all()
    myapi.customer_del_all()
    myapi.medicines_del_all()
    myapi.medicines_add( "青霉素","青霉素 国字号","234324234234")
def suite_teardown():
    myapi.medicines_del_all()
force_tags=['删除药品功能']
class c0323:
    name='删除药品 -api0323'
    def teststeps(self):
        STEP(1,'删除操作')
        r=myapi.medicines_list().json()
        addid = r["retlist"][0]["id"]
        res=myapi.medicines_del(addid)
        STEP(2,'检查操作')
        CHECK_POINT('检查消息体内容',res.json()==
                    {
                        "ret": 0
                    })