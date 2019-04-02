# truck.py
# 卡车类，演示运算符重载
class Truck:
    def __init__(self, load):
        self.load = load #载重

    def __add__(self, value):#重载+运算符
        print("__add__()被调用")
        return Truck(self.load + value)

    def __mul__(self, value): #重载*运算符
        return Truck(self.load * value)

    #反向+运算符重载，支持 3 + truck操作
    def __radd__(self, value): 
        print("__radd__()被调用")
        return Truck(self.load + value)

    # 符合运算符重载，支持obj += 2表达式
    # def __iadd__(self, value):
    #     print("__iadd__()被调用")
    #     return Truck(self.load + value)

    def __str__(self):
        return "load: %d" % self.load

    def __gt__(self, other): # 重载>运算符
        print("__gt__()方法被调用")
        if self.load > other.load:
            return True
        else:
            return False

    # def __lt__(self, other): # 重载<运算符
    #     if self.load < other.load:
    #         return True
    #     else:
    #         return False

if __name__ == "__main__":
    t1 = Truck(20)
    t2 = Truck(25)
    print(t1 > t2)  # 调用__gt__()
    print(t1 < t2)  # 调用__lt__()
    #t = Truck(20)
    #t2 = t + 1 # t2接受返回的对象
    #t2 = 1 + t  # 调用__radd__（）方法
    # t += 1 # 调用__iadd__()方法，如果没有该方法，调用__add__
    # print(t)
    # t3 = t * 4 
    # print(t3)