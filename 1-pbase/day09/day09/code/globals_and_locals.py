# globals_and_locals.py


# 此示例示意globals 和 locals函数的使用方法
a = 1
b = 2
c = 3
def fn(c, d):
    e = 300
    # 此处有多少个局部变量?
    print("locals()返回:", locals())
    # 此处有多少个全局变量?
    print("globals() 返回:", globals())
    print(c)  # 100
    print(globals()['c'])  # 3


fn(100, 200)
