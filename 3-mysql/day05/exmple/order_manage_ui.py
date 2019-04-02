# order_manage_ui.py
# 订单管理用户接口层(视图层)
# 只负责用户发出命令　显示执行结果
from db_oper import *
from order import *
from order_manage import *

db_oper = None
om = None
def print_menu():
    menu = '''
    ----------订单管理页面---------
        1- 查询所有订单
        2- 根据订单号查询
        3- 新增订单
        4- 删除订单
        5- 退出
    '''

    print(menu)



def query_all_order():
    order_list = om.query_all_order()
    for a in order_list:
        print(a)

def query_orders():
    order_list = []
    while True:
        order_id = input("请输入要查询的订单编号:")
        if not order_id:
            print("输入非法账号")
        else:
            order_list.append.order_id
            for order_id in order_list:
                order= om.query_orders(order_id)
                
                print(order)

    
def insert_orders():
    # order_id = input('请输入要新曾的订单编号:')
    # cust_id = input(''
    pass

def delete_orders():
    pass

def main():
    global db_oper
    global am
    db_oper = DBOper()
    db_oper.open_conn()
    om = OrderManage(db_oper)

    while True:
        print_menu()
        oper = input("请选择要执行的操作:")

        if oper == '1':
            query_all_order()
        elif oper =='2':
            query_orders()
        elif oper =='3':
            insert_orders()
        elif oper =='4':
            delete_orders()
        elif oper =='5':
            break
    db_oper.close_conn()


if __name__ = '__main__':
    main()























