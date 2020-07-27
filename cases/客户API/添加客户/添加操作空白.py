from lib.API import myapi
from hyrobot.common import  *
def suite_setup():
    myapi.login()
    myapi.orders_del_all()
    myapi.customer_del_all()
    myapi.medicines_del_all()
def suite_teardown():
    myapi.customer_del_all()
force_tags=['添加用户功能']
class c0207:
    def teardown(self):
        myapi.customer_del(self.addid)
    name='添加操作 -api0207'
    def teststeps(self):
        STEP(1,'添加用户')
        r=myapi.customer_add("武汉市桥西医院","13345679934","武汉市桥西医院北路")
        self.addid=r.json()['id']
        CHECK_POINT('ret的值',r.json()["ret"]==0)
        STEP(2,'检查操作')
        res=myapi.customer_list().json()
        expected = {
                "ret": 0,
                "retlist": [
                    {
                    "address": "武汉市桥西医院北路",
                    "id": self.addid,
                    "name": "武汉市桥西医院",
                    "phonenumber": "13345679934"
                    }
            ],
            'total':1
            }

        CHECK_POINT('返回消息体内容', expected==res)
class c0208:
    name='添加操作 -api0208'
    def teststeps(self):
        STEP(1, '添加用户')
        r = myapi.customer_add("13345679934", "武汉市桥西医院北路")
        STEP(2, '检查操作')
        CHECK_POINT('返回消息体内容',r.json()==
                                {
                        "ret": 1,
                        "msg":  "请求消息参数错误",
                                })

class c0209:
    name = '添加操作 -api0209'
    def teststeps(self):
        STEP(1, '添加用户')
        r = myapi.customer_add('wxl', "武汉市桥西医院北路")
        STEP(2, '检查操作')
        CHECK_POINT('返回消息体内容', r.json() ==
                    {
                        "ret": 1,
                        "msg": "请求消息参数错误",
                    })
class c0210:
    name='添加操作 -api0210'
    def teststeps(self):
        STEP(1, '添加用户')
        r = myapi.customer_add('wxl',"13345679934")
        STEP(2, '检查操作')
        CHECK_POINT('返回消息体内容', r.json() ==
                    {
                        "ret": 1,
                        "msg": "请求消息参数错误",
                    })










