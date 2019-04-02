# bird.py
# 鸟类
class Bird:
    def __init__(self, name):
        self.name = name
    
    def eat(self):  # 吃方法
        print("%s正在吃饭" % self.name)

    def fly(self):  # 飞行
        print("%s正在飞行" % self.name)

    def reproduction(self): # 繁殖
        print("%s是卵生" % self.name)

class Eagle(Bird):  # 老鹰类，继承自Bird
    def eat(self):   # 重写eat方法
        print("我是%s,我喜欢吃肉" % self.name)

    def fly(self): 
        print("我是%s,飞的又高又快" % self.name)

class Ostrich(Bird):  # 鸵鸟类，继承自Bird
    def fly(self):  # 重写fly方法
        print("我是%s,太重了不能飞" % self.name)

    def eat(self):
        print("我是%s,我是杂事动物" % self.name)

if __name__ == "__main__":
    eagle = Eagle("老鹰")
    eagle.eat()
    eagle.fly()
    eagle.reproduction()
    print("")
    ostrich = Ostrich("鸵鸟")
    ostrich.eat()
    ostrich.fly()
    ostrich.reproduction()
