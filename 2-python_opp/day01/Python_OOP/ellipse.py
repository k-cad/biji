# ellipse.py
# 面向过程、面向对象编程比较
# 计算椭圆周长、面积

# 面向过程方式
a = 2.0   # 短半径
b = 3.0   # 长半径
len = 2 * 3.14 * a + 4 * (b - a) 
print("a=%f, b=%f, len=%f" % (a,b,len))  

area = 3.14 * a * b
print("a=%f, b=%f, area=%f" % (a,b,area)) 

# 面向对象方式
class Ellipse:   # 定义椭圆类
    #类中的函数, 称之为方法
    def __init__(self, a, b):  # 构造方法
        self.a = a   # 属性：短半径
        self.b = b   # 属性：长半径
    # 2 * pi * 短半径 + 4（长半径 - 短半径）
    def calc_len(self): #计算周长
        return 2 * 3.14 * self.a + \
               4 * (self.b - self.a)
    
    def calc_area(self): #计算面积
        return 3.14 * self.a * self.b

e = Ellipse(2.0, 3.0)  # 实例化：创建椭圆对象
len = e.calc_len()     # 获得椭圆周长
area = e.calc_area()   # 获得椭圆面积
print("a=%f，b=%f, len=%f, area=%f" %
      (e.a, e.b, len, area))



    