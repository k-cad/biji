#订单管理类,业务逻辑层
from db_oper import *
from order import *

class OrderManage:
    # 构造方法
    def __init__(self,db_oper):
        self.db_oper = db_oper#在属性中保存数据操作对象
    #查询所有订单信息
    def query_all_order(self):
        order_list = []
        sql = "select * from orders"
        result = self.db_oper.do_query(sql)
        if not result:
            print("查询返回空对象")
            return None
        for order_info in result:
            order_id = order_info[0]
            cust_id = order_info[1]
            if order_info[5]:
                amt = float(order_info[5])
            else:
                amt = 0.00
            order_list.append(Order(order_id,cust_id,amt))
        
        return order_list
    def query_orders(self,order_id):
        if not order_id:
            print("订单号错误")
        elif order_id == "":
            print('非法订单')
        sql = "select * from orders where order_id ='%s'" % order_id
        order_info = self.db_oper.do_query(sql)
        print(order_info)
        if not order_info:
            print("该订单不在")
            return order_id
        else:
            order_id = order_info[0][0]
            cust_id = order_info[0][1]
            if order_info[0][5]:
                amt = float(order_info[0][5])
            else:
                amt = 0.00
            return Order(order_id,cust_id,amt)


    # def add_new_order(self,)

if __name__ == "__main__":
    db_oper = DBOper()
    db_oper.open_conn()

    om = OrderManage(db_oper)
    query_one_order(2018010100000007)
      # order_list = om.query_all_order()
    # for o in order_list:
    #     print(o)
    db_oper.close_conn()
