# 练习:
#   已知内建函数max帮助文档为:
#     max(...)
#         max(iterable) -> value
#         max(arg1, arg2, *args) -> value
#   仿造 max写一个mymax函数,功能与max完全相同
#     (要求不允许调用max)
#   测试程序如下:
#      print(mymax([6, 8, 3, 5]))  # 8
#      print(mymax(100, 200))      # 200
#      print(mymax(1, 3, 5, 9, 7)) # 9


def mymax(a, *args):
    if len(args) == 0:  # 判断是否是一个可迭代参数的情况
        L = a  # 一定绑定一个可迭代对象
        zuida = L[0]  # 假设第一个元素最大
        for x in L:
            if x > zuida:
                zuida = x
        return zuida
    else:  # 否则有多个参数的情况
        zuida = a
        for x in args:
            if x > zuida:
                zuida = x
        return zuida


print(mymax([6, 8, 3, 5]))  # 8
print(mymax(100, 200))      # 200
print(mymax(1, 3, 5, 9, 7)) # 9



