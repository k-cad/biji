#作业：
#1)定义一个鸟类(Bird),具有吃(eat),飞行(fly),繁殖(reproduction)方法
#2)定义老鹰类(Eagle),鸵鸟类(Ostrich)类,继承自Bird类
#3)编写测试代码，测试eat,fly,reproduction方法
class Bird:
    def __init__(self,name,food,speed,egg_counts):
        self.name = name
        self.food = food
        self.speed = speed
        self.egg_counts = egg_counts

    def eat(self):
        print('%s吃%s' % (self.name,self.food))

    def fly(self):
            print("%s每小时飞行%d公里"%(self.name,self.speed))

    def reproduction(self):
        print("每年繁殖%d个蛋" % self.egg_counts)