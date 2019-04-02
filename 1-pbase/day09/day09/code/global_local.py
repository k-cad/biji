# global_local.py

# 此示例示意全局变量的定义和局部变量的定义
a = 100
b = 200
c = 9999999
def fx(c):
    a = 1  # 创建局部变量,并非改变全局变量
    d = 400
    print(a, b, c, d)

fx(300)
print('a=', a)  # 100
print('b=', b)
print('c=', c)