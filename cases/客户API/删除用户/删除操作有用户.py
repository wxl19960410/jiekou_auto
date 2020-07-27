from lib.API import myapi
from hyrobot.common import  *
def suite_setup():
    myapi.login()
    myapi.orders_del_all()
    myapi.customer_del_all()
    myapi.medicines_del_all()
    myapi.customer_add('wxl','123456789','nanjingyoudiandaxue')
def suite_teardown():
    myapi.medicines_del_all()
force_tags=['删除用户功能']
class c0223:
    name='删除用户 -api0223'
    def teststeps(self):
        STEP(1,'删除操作')
        r=myapi.customer_list().json()
        addid = r["retlist"][0]["id"]
        res=myapi.customer_del(addid)
        STEP(2,'检查操作')
        CHECK_POINT('检查消息体内容',res.json()==
                    {
                        "ret": 0
                    })

