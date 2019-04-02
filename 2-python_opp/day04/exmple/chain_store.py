#chain_store.py
#连锁店类,类属性/类方法示例
from staff import *
from customer import *

class ChainStore:
    # 类属性
    store_num = 0
    total_income = 0
    store_list = []
    cust_list = []
    
    def __init__(self,store_no,store_name,address,manager):
        print('门店开张')
        self.store_no = store_no#编号
        self.store_name = store_name
        self.address = address
        self.manager = manager
        self.myincome = 0 
        ChainStore.store_num += 1
        ChainStore.store_list.append(self)
        self.staff_list = []

    def add_staff(self,staff):
        self.staff_list.append(staff)

    def remove_staff(self,NO):
        for staff in self.staff_list:
            if staff.NO == NO:
                self.staff_list.remove(staff)
            
    def print_all_staff(self):
        for staff in self.staff_list:
            print(staff)    

    def do_business(self,income):
        print('正在营业')
        self.myincome += income
        ChainStore.total_income += income

    def __str__(self):
        ret = "编号:%s,名称:%s,地址:%s,店长:%s,总营业额:%.2f"\
             %(self.store_no,self.store_name,self.address,self.manager,self.myincome)
        return ret
    
    def __del__(self):
        print('%s门店关闭'%self.store_name)
        ChainStore.store_num -= 1


    @classmethod
    def print_total(cls):#类方法，打印类的属性
        print("门店数量：%d,营业总额度：%.2f"%(cls.store_num,cls.total_income))
        for store in cls.store_list:
            print(str(store))

    @staticmethod
    def print_regulation():
        regulation = '''
        ---------门店管理条例----------
        第一条
        第二条
        ...
        '''
        print(regulation)

    def cust_reg(self,cust):#会员属性
        ChainStore.cust_list.append(cust)

    def print_cust_info(self):#打印会员
        for cust in ChainStore.cust_list:
            print(cust)

if __name__ == "__main__":
    store1 = ChainStore('1',"西单旗舰店",'西单','张大大')
    store1.do_business(20000)
    store1.add_staff(Staff('00001','Jerry','店长'))
    store1.add_staff(Staff('00002','Tom','店员'))
    store1.add_staff(ServiceRobot('00003','Alph','服务员'))
    store1.print_all_staff()

    store1.cust_reg(Customer('1','八戒',213465765))
    store1.cust_reg(Customer('2','wukong',21387595))
    store1.print_cust_info()
    # print('门店数量:',ChainStore.store_num)
    # print("总营业额度:",ChainStore.total_income)
    ChainStore.print_total()
    ChainStore.print_regulation()
    print('')

    store2 = ChainStore('2',"中关村店",'中关村','王小小')
    store2.do_business(15000)
    del store2 #销毁店铺２
    # print('门店数量:',ChainStore.store_num)
    # print("总营业额度:",ChainStore.total_income)
    ChainStore.print_total()
    store2.print_regulation()



















