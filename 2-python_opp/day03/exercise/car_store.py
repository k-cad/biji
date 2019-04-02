# -*- coding:utf-8 -*-
#car_store.py
#汽车租赁模拟程序
class Car:
    def __init__(self,car_id,name,price,is_lend):
        self.car_id = car_id #车辆编码
        self.name  = name #名称
        self.price = price #价格
        self.is_lend = is_lend #是否出租
        self.start_data = ""#起租日期
        self.end_data = ""#预计归还日期
        self.cust_id = ""#客户编码
    
    def __str__(self):
        ret = "车辆编号:%s,名称:%s,单价:%.2f,是否出租:%s" \
            % (self.car_id,self.name,self.price,self.is_lend)
        return ret

class Customer:
    def __init__(self,cust_id,cust_name,TEL_NO):
        self.cust_id = cust_id
        self.cust_name = cust_name
        self.TEL_NO = TEL_NO

    def __str__(self):
        ret = "客户编码:%s,客户名称:%s,电话:%s"\
            %(self.cust_id,self.cust_name,self.TEL_NO)

class CarStore:
    def __init__(self):
        self.cars = []#车辆列表
        self.customers = []
        self.__load_cars()
        self.__load_customers()

    def __load_cars(self):#加载车辆列表
        self.cars.append(Car('1','Golf',400,"否"))
        self.cars.append(Car('2','凯越',350,"否"))
        self.cars.append(Car('3','奥迪',1200,"否"))
        self.cars.append(Car('4','凯美瑞',800,"否"))
        self.cars.append(Car('5','宝来',450,"否"))
    
    def __load_customers(self):#记载客户列表
        cust1 = Customer("C001","张三",'12345')
        cust2 = Customer("C002","张四",'12356')
        cust3 = Customer("C003","张五",'12367')
        
        self.customers.append(cust1)
        self.customers.append(cust2)
        self.customers.append(cust3)

    def print_cars_info(self):
        for car in self.cars:
            print(car)
    
    def find_car(self,car_id):#根据车辆编号查询
        for car in self.cars:
            if car.car_id == car_id:
                print(car)
                return
        print('未找到该车辆')
        return

    def add_car(self,car):
        if isinstance(car,Car):
            self.cars.append(car)
        else:
            print("对象类型错误")
        return

    def del_car(self,car_id):
        for car in self.cars:
            if car.car_id == car_id:
                self.cars.remove(car)
        return

    def len(self,car_id,cust_id,start_data,end_data):
        for car in self.cars:
            if car.car_id == car_id:
                if car.is_lend == "是":
                    print("该车已出租")
                    return
                else:
                    setattr(car,"is_lend","是")
                    setattr(car,'cust_id',cust_id)
                    setattr(car,'start_data',start_data)
                    setattr(car,'end_data',end_data)
                    print('车辆出租登记完成')
                    return
        print('未找到车辆信息')
        return

    def back(self,car_id):
        for car in self.cars:
            if car.car_id == car_id:
                setattr(car,"is_lend","否")
                setattr(car,'cust_id','')
                setattr(car,'start_data','')
                setattr(car,'end_data','')
                print('还车登记完成')
                return
        print('未找到该车辆信息')
        return

if __name__ == "__main__":
    car_store = CarStore()
    # car_store.print_cars_info()
    # print('')
    # car_store.find_car('3')
    # print('')
    # car = Car('6','捷达',300,"否")
    # car_store.add_car(car)
    # car_store.print_cars_info()
    # car_store.del_car('3')
    # car_store.print_cars_info()
    car_store.len("3","C0001",'2018-01-03','2018-01-05')
    car_store.print_cars_info()
    car_store.back('3')
    car_store.print_cars_info()
    