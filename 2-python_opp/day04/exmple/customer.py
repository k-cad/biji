#客户类
class Customer:
    def __init__(self,cust_id,cust_name,TEL_NO):
        self.cust_id = cust_id
        self.cust_name = cust_name
        self.TEL_NO = TEL_NO

    def __str__(self):
        ret = "客户编码:%s,客户名称:%s,电话:%s"\
            %(self.cust_id,self.cust_name,self.TEL_NO)
        return ret
        