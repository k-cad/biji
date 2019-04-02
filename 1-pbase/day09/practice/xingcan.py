#已知内建函数max的帮助文档为：
#max(...)
# max(iterable, *[, default=obj, key=func]) -> value
# max(arg1, arg2, *args, *[, key=func]) -> value
#仿造max写一个mymax函数，功能与max完全相同
# def mymax(*args):
#     if len(args)==1:#判断是否是一个可迭代参数的情况
#         L=args[0]
#         m=L[0]
#         for x in L:
#             if x > m:
#                 m=x
#         return m
#     else:
#         m=args[0]
#         for x in args:
#             if x>m:
#                 m=x
#         return m

# print(mymax([6,8,3,5]))
# print(mymax(100,200))
# print(mymax(1,3,5,7,9))


def mymax(a,*args):
    if len(args)==0:
        L=a
        m=L[0]
        for x in L:
            if x > m:
                m=x
        return m
    else:
        m=a
        for x in args:
            if x>m:
                m=x
        return m

print(mymax([6,8,3,5]))
print(mymax(100,200))
print(mymax(1,3,5,7,9))
