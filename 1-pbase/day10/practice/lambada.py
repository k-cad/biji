#1， 写一个lambda表达式,判断n的2次方能否被5整除
# fx = lambda n:(n**2+1)%5==0

# print(fx(3))
# print(fx(4))     

# 2，写一个lambda表达式来创建函数，此函数返回两个形参变量的最大值

# def mymax(x,y):
#     return x if x>=y else y
mymax = lambda x,y: x if x>=y else y
    
