#订单类，接受数据库中的订单记录中的值
class Order:
    def __init__(self,order_id,cust_id,amt):
        self.order_id = order_id
        self.cust_id = cust_id
        self.amt = amt

    def __str__(self):
        ret = "订单号:%s,客户:%s,金额:%.2f"%(self.order_id,self.cust_id,self.amt)
        return ret
        