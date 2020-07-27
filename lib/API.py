import  requests,json
from hyrobot.common import *
class MYAPI():
    #打印响应信息
    def print_response(self,response):
        INFO(response.status_code)
        for k ,v in response.headers.items():
            INFO('{0}:{1}'.format(k,v))
        INFO(response.content.decode('utf8'))

    #登录
    def login(self,username='byhy',password='88888888',useproxies=False):
        self.s=requests.Session()
        if useproxies:
            self.s.proxies.update({'http':'http://127.0.0.1:8888'})
        response=self.s.post(url='http://127.0.0.1/api/mgr/signin',
                            data = {
                                    'username': username,
                                    'password': password
                                }
                           )
        self.print_response(response)
        return response
###客户操作
    #列出客户
    def customer_list(self,pagesize=10,pagenum=1,keywords=''):
        response=self.s.get(url='http://127.0.0.1/api/mgr/customers',params=
        {
            'action':'list_customer',
            'pagesize':pagesize,
            'pagenum':pagenum,
            'keywords':keywords
        })
        self.print_response(response)
        return response

    #添加用户
    def customer_add(self,name,phonenumber,address):
        response=self.s.post(url="http://127.0.0.1/api/mgr/customers",
                                json={
                                        "action": "add_customer",
                                         "data":{
                                                "name":name,
                                                "phonenumber":phonenumber,
                                                "address":address
                                                 }
                                        })

        self.print_response(response)
        return response

    #修改用户
    def customer_alter(self,cid,name,phonenumber,address):
        response=self.s.put(url="http://127.0.0.1/api/mgr/customers",json={
                                        "action": "modify_customer",
                                        "id": cid,
                                        "newdata":{
                                                "name":name,
                                                "phonenumber":phonenumber,
                                                "address":address
                                                 }
                                        })
        self.print_response(response)
        return response
    #删除用户
    def customer_del(self,cid):
        response = self.s.delete(url="http://127.0.0.1/api/mgr/customers", json=
        {
            "action": "del_customer",
            "id": cid
        })
        self.print_response(response)
        return response
    #删除所有用户
    def customer_del_all(self):
        response=self.customer_list(100,1,'')
        alllist=response.json()["retlist"]
        for each in alllist:
            self.customer_del(each["id"])

###药品操作

    #列出药品
    def medicines_list(self,pagesize=10,pagenum=1,keywords=''):
        response=self.s.get(url='http://127.0.0.1/api/mgr/medicines',params=
        {
            'action':'list_medicine',
            'pagesize':pagesize,
            'pagenum':pagenum,
            'keywords':keywords
        })
        self.print_response(response)
        return response

    #添加药品
    def medicines_add(self,name,desc,sn):
        response=self.s.post(url="http://127.0.0.1/api/mgr/medicines",
                                json={
                                        "action": "add_medicine",
                                         "data":{
                                                "name":name,
                                                "desc":desc,
                                                "sn":sn
                                                 }
                                        })

        self.print_response(response)
        return response

    #修改药品
    def medicines_alter(self,mid,name,desc,sn):
        response=self.s.put(url="http://127.0.0.1/api/mgr/medicines",json={
                                        "action": "modify_medicine",
                                        "id": mid,
                                        "newdata":{
                                                "name":name,
                                                "desc":desc,
                                                "sn":sn
                                                 }
                                        })
        self.print_response(response)
        return response
    #删除药品
    def medicines_del(self,mid):
        response = self.s.delete(url="http://127.0.0.1/api/mgr/medicines", json={
            "action":"del_medicine",
            "id": mid
        })
        self.print_response(response)
        return response
    #删除所有药品
    def medicines_del_all(self):
        response=self.medicines_list(100,1,'')
        alllist=response.json()["retlist"]
        for each in alllist:
            self.medicines_del(each["id"])




###订单操作

    #列出订单
    def orders_list(self,pagesize=10,pagenum=1,keywords=''):
        response=self.s.get(url='http://127.0.0.1/api/mgr/orders',params=
        {
            'action':'list_order',
            'pagesize':pagesize,
            'pagenum':pagenum,
            'keywords':keywords
        })
        self.print_response(response)
        return response

    #添加订单
    def orders_add(self,name,customerid,medicinelist):

        response=self.s.post(url="http://127.0.0.1/api/mgr/orders",
                                json={
                                        "action":"add_order",
                                        "data":{
                                            "name":name,
                                            "customerid":customerid,
                                            "medicinelist":medicinelist
                                                }
                                        })

        self.print_response(response)
        return response
    #删除订单
    def orders_del(self,oid):
        response = self.s.delete(url="http://127.0.0.1/api/mgr/orders", json={
            "action": "delete_order",
            "id": oid
        })
        self.print_response(response)
        return response
    #删除所有订单
    def orders_del_all(self):
        response=self.orders_list(100,1,'')
        alllist=response.json()["retlist"]
        for each in alllist:
            self.orders_del(each["id"])

myapi=MYAPI()





















