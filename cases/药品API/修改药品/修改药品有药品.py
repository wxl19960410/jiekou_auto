from lib.API import myapi
from hyrobot.common import  *
def suite_setup():
    myapi.login()
    myapi.orders_del_all()
    myapi.customer_del_all()
    myapi.medicines_del_all()
    myapi.medicines_add('青霉素','青霉素 国字号','099877883837')
def suite_teardown():
    myapi.medicines_del_all()
force_tags=['修改药品功能']
class c0314:
    name='修改药品 -api0314'
    def teardown(self):
        r = myapi.medicines_list().json()
        addid = r["retlist"][0]["id"]
        res = myapi.customer_alter(addid,'青霉素','青霉素 国字号','099877883837')
    def teststeps(self):
        STEP(1,'修改药品')
        r=myapi.medicines_list().json()
        addid=r["retlist"][0]["id"]
        res=myapi.medicines_alter(addid,'青霉素1','青霉素 国字号','099877883837')
        STEP(2,'检查操作')
        CHECK_POINT('检查消息体',res.json()=={
                                                "ret": 0})
class c0315:
    name='修改药品 -api0315'
    def teardown(self):
        r = myapi.medicines_list().json()
        addid = r["retlist"][0]["id"]
        res = myapi.customer_alter(addid,'青霉素','青霉素 国字号','099877883837')
    def teststeps(self):
        STEP(1,'修改药品')
        r=myapi.medicines_list().json()
        addid=r["retlist"][0]["id"]
        res=myapi.medicines_alter(addid,'青霉素','青霉素 国字号1','099877883837')
        STEP(2,'检查操作')
        CHECK_POINT('检查消息体',res.json()=={
                                                "ret": 0})
class c0316:
    name='修改药品 -api0316'
    def teardown(self):
        r = myapi.medicines_list().json()
        addid = r["retlist"][0]["id"]
        res = myapi.customer_alter(addid,'青霉素','青霉素 国字号','099877883837')
    def teststeps(self):
        STEP(1,'修改药品')
        r=myapi.medicines_list().json()
        addid=r["retlist"][0]["id"]
        res=myapi.medicines_alter(addid,'青霉素','青霉素 国字号','099877883838')
        STEP(2,'检查操作')
        CHECK_POINT('检查消息体',res.json()=={
                                                "ret": 0})

class c0317:
    name='修改药品 -api0317'
    def teardown(self):
        r = myapi.medicines_list().json()
        addid = r["retlist"][0]["id"]
        res = myapi.customer_alter(addid,'青霉素','青霉素 国字号','099877883837')
    def teststeps(self):
        STEP(1,'修改药品')
        r=myapi.medicines_list().json()
        addid=r["retlist"][0]["id"]
        res=myapi.medicines_alter(addid,'青霉素1','青霉素 国字号gdg','099877883837')
        STEP(2,'检查操作')
        CHECK_POINT('检查消息体',res.json()=={
                                                "ret": 0})
class c0318:
    name='修改药品 -api0318'
    def teardown(self):
        r = myapi.medicines_list().json()
        addid = r["retlist"][0]["id"]
        res = myapi.customer_alter(addid,'青霉素','青霉素 国字号','099877883837')
    def teststeps(self):
        STEP(1,'修改药品')
        r=myapi.medicines_list().json()
        addid=r["retlist"][0]["id"]
        res=myapi.medicines_alter(addid,'青霉素韩国','青霉素 国字号','099877883840')
        STEP(2,'检查操作')
        CHECK_POINT('检查消息体',res.json()=={
                                                "ret": 0})
class c0319:
    name='修改药品 -api0319'
    def teardown(self):
        r = myapi.medicines_list().json()
        addid = r["retlist"][0]["id"]
        res = myapi.customer_alter(addid,'青霉素','青霉素 国字号','099877883837')
    def teststeps(self):
        STEP(1,'修改药品')
        r=myapi.medicines_list().json()
        addid=r["retlist"][0]["id"]
        res=myapi.medicines_alter(addid,'青霉素','青霉素 国字号好好干','099877883845')
        STEP(2,'检查操作')
        CHECK_POINT('检查消息体',res.json()=={
                                                "ret": 0})
class c0320:
    name='修改药品 -api0320'
    def teardown(self):
        r = myapi.medicines_list().json()
        addid = r["retlist"][0]["id"]
        res = myapi.customer_alter(addid,'青霉素','青霉素 国字号','099877883837')
    def teststeps(self):
        STEP(1,'修改药品')
        r=myapi.medicines_list().json()
        addid=r["retlist"][0]["id"]
        res=myapi.medicines_alter(addid,'青霉素115','青霉素 国字号好好干','099877883848')
        STEP(2,'检查操作')
        CHECK_POINT('检查消息体',res.json()=={
                                                "ret": 0})
class c0321:
    name='修改药品 -api0321'
    def teststeps(self):
        STEP(1,'修改药品')
        r=myapi.medicines_list().json()
        addid=r["retlist"][0]["id"]
        res=myapi.medicines_alter(addid,'青霉素','青霉素 国字号','099877883837')
        STEP(2,'检查操作')
        CHECK_POINT('检查消息体',res.json()["ret"]==0)







