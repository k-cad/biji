此示例示意全局变量的定义和局部变量的定义
a=100
b=200
def fx(c):
    d=400
    print(a,b,c,d)
fx(300)
print('a=',a)
print('b=',b)
# print('c=',c)c出错