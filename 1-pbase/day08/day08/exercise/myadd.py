# 练习:
#   写一个函数myadd,此函数中的参数列表里有两个参数x,y
#   此函数的功能是打印 x + y 的和
#   如:
#     def myadd(...):
#         ...  # ...部分自己实现
#     myadd(100, 200)   # 打印 300
#     myadd("ABC", "123")  # 打印 ABC123


def myadd(x, y):
    z = x + y
    print('和是:', z)

myadd(100, 200)   # 打印 300
myadd("ABC", "123")  # 打印 ABC123

# print(z)  # 报错!
# print(x)
# print(y)