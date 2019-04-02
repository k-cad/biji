#面向过程方式
# a=2.0
# b=3.0
# len=2*3.14*a+4*(b-a)
# arae=3.14*a*b
# print('a=%f,b=%f,len=%f,area=%f'%(a,b,len,arae))

#面向对象方式
class Ellipse:#定义椭圆类
    #类中的函数，称之为方法
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def calc_len(self):
        return 2*3.14*self.a+\
               4*(self.b-self.a)
    def calc_area(self):
        return 3.14*self.a*self.b

e=Ellipse(2.0,3.0)#实例化：创建椭圆对象
len=e.calc_len()
arae=e.calc_area()
print('a=%f,b=%f,len=%f,area=%f'%(e.a,e.b,len,arae))