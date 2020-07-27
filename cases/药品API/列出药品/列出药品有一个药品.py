from lib.API import myapi
from hyrobot.common import  *

def suite_setup():
    myapi.login()
    myapi.orders_del_all()
    myapi.customer_del_all()
    myapi.medicines_del_all()
    myapi.medicines_add( "青霉素","青霉素 国字号","099877883837")
def suite_teardowm():
    myapi.medicines_del_all()

force_tags=['列出药品功能']
class c0305:
    name='列出 api-0305'
    def teststeps(self):
        STEP(1,'列出操作')
        response=myapi.medicines_list()
        STEP(2,'检查操作')
        CHECK_POINT('检查返回消息体ret',response.json()["ret"]==0)
        CHECK_POINT('检查返回消息体total', response.json()["total"] == 1)