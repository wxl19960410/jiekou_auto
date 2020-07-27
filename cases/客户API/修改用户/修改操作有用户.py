from lib.API import myapi
from hyrobot.common import  *
def suite_setup():
    myapi.login()
    myapi.orders_del_all()
    myapi.customer_del_all()
    myapi.medicines_del_all()
    myapi.customer_add('wxl','123456789','nanjingtoudiandaxue')
def suite_teardown():
    myapi.customer_del_all()
force_tags=['修改用户功能']
class c0214:
    name='修改用户 -api0214'
    def teardown(self):
        r = myapi.customer_list().json()
        addid = r["retlist"][0]["id"]
        res = myapi.customer_alter(addid, 'wxl', 123456789, 'nanjingtoudiandaxue')
    def teststeps(self):
        STEP(1,'修改操作')
        r=myapi.customer_list().json()
        addid=r["retlist"][0]["id"]
        res=myapi.customer_alter(addid,'wxl1',123456789,'nanjingtoudiandaxue')
        STEP(2,'检查操作')
        CHECK_POINT('检查消息体',res.json()=={
                                                "ret": 0})
class c0215:
    name='修改用户 -api0215'
    def teardown(self):
        r = myapi.customer_list().json()
        addid = r["retlist"][0]["id"]
        res = myapi.customer_alter(addid, 'wxl', 123456789, 'nanjingtoudiandaxue')
    def teststeps(self):
        STEP(1,'修改操作')
        r=myapi.customer_list().json()
        addid=r["retlist"][0]["id"]
        res=myapi.customer_alter(addid,'wxl',12345678,'nanjingtoudiandaxue')
        STEP(2,'检查操作')
        CHECK_POINT('检查消息体',res.json()=={
                                                "ret": 0})
class c0216:
    name='修改用户 -api0216'
    def teardown(self):
        r = myapi.customer_list().json()
        addid = r["retlist"][0]["id"]
        res = myapi.customer_alter(addid, 'wxl', 123456789, 'nanjingtoudiandaxue')
    def teststeps(self):
        STEP(1,'修改操作')
        r=myapi.customer_list().json()
        addid=r["retlist"][0]["id"]
        res=myapi.customer_alter(addid,'wxl',123456789,'nanjing')
        STEP(2,'检查操作')
        CHECK_POINT('检查消息体',res.json()=={
                                                "ret": 0})
class c0217:
    name='修改用户 -api0217'
    def teardown(self):
        r = myapi.customer_list().json()
        addid = r["retlist"][0]["id"]
        res = myapi.customer_alter(addid, 'wxl', 123456789, 'nanjingtoudiandaxue')
    def teststeps(self):
        STEP(1,'修改操作')
        r=myapi.customer_list().json()
        addid=r["retlist"][0]["id"]
        res=myapi.customer_alter(addid,'wxl1',1234567891,'nanjingtoudiandaxue')
        STEP(2,'检查操作')
        CHECK_POINT('检查消息体',res.json()=={
                                                "ret": 0})
class c0218:
    name='修改用户 -api0218'
    def teardown(self):
        r = myapi.customer_list().json()
        addid = r["retlist"][0]["id"]
        res = myapi.customer_alter(addid, 'wxl', 123456789, 'nanjingtoudiandaxue')
    def teststeps(self):
        STEP(1,'修改操作')
        r=myapi.customer_list().json()
        addid=r["retlist"][0]["id"]
        res=myapi.customer_alter(addid,'wxl1',123456789,'nanjingtoudiandaxue123')
        STEP(2,'检查操作')
        CHECK_POINT('检查消息体',res.json()=={
                                                "ret": 0})
class c0219:
    name='修改用户 -api0219'
    def teardown(self):
        r = myapi.customer_list().json()
        addid = r["retlist"][0]["id"]
        res = myapi.customer_alter(addid, 'wxl', 123456789, 'nanjingtoudiandaxue')
    def teststeps(self):
        STEP(1,'修改操作')
        r=myapi.customer_list().json()
        addid=r["retlist"][0]["id"]
        res=myapi.customer_alter(addid,'wxl',123456789123,'nanjingtoudiandaxuexsa')
        STEP(2,'检查操作')
        CHECK_POINT('检查消息体',res.json()=={
                                                "ret": 0})

class c0220:
    name='修改用户 -api0220'
    def teardown(self):
        r = myapi.customer_list().json()
        addid = r["retlist"][0]["id"]
        res = myapi.customer_alter(addid, 'wxl', 123456789, 'nanjingtoudiandaxue')
    def teststeps(self):
        STEP(1,'修改操作')
        r=myapi.customer_list().json()
        addid=r["retlist"][0]["id"]
        res=myapi.customer_alter(addid,'wxl1',123456789112,'nanjingtoudiandaxuesasdf')
        STEP(2,'检查操作')
        CHECK_POINT('检查消息体',res.json()=={
                                                "ret": 0})
class c0221:
    name='修改用户 -api0221'
    def teststeps(self):
        STEP(1,'修改操作')
        r=myapi.customer_list().json()
        addid=r["retlist"][0]["id"]
        res=myapi.customer_alter(addid,'wxl',123456789,'nanjingtoudiandaxue')
        STEP(2,'检查操作')
        CHECK_POINT('检查消息体',res.json()["ret"]==0)





