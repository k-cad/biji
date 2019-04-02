# truck.py
# 卡车类，演示运算符重载
class Truck:
    def __init__(self,load):
        self.load = load
    def __add__(self,value):
        return Truck(self.load + value)

    def __mul__(self,value):
        return Truck(self.load * value)

    def __str__(self.load + value):
        return "load:%d" % self.data

if __name__ == "__main__":
    t = Truck(20)
    t2 = t + 1
    print(t2)
    t3 = t * 4
    print(t3)



























