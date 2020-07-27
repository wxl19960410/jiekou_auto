from lib.API import myapi
from hyrobot.common import  *

def suite_setup():
    myapi.login()
    myapi.orders_del_all()
    myapi.customer_del_all()
    myapi.medicines_del_all()
    myapi.customer_add('wxl','15563523563','南京鼓楼区邮电大学')
def suite_teardowm():
    myapi.customer_del_all()

force_tags=['列出用户功能']
class c0205:
    name='列出 api-0205'
    def teststeps(self):
        STEP(1,'列出操作')
        response=myapi.customer_list()
        STEP(2,'检查操作')
        CHECK_POINT('检查返回消息体ret',response.json()["ret"]==0)
        CHECK_POINT('检查返回消息体total', response.json()["total"] == 1)

