# 练习:
#   1. 写一个生成器函数myeven(begin, end), 用来生成从begin开始
#      到end结束的所有偶数(不包含end)
#     如:
#         def myeven(begin, end):
#             ... 此处自己实现

#         for x in myeven(1, 10):
#             print(x)  # 打印 2, 4, 6, 8
#         L = [x**2 for x in myeven(4, 9)]
#         print(L)  # [16, 36, 64]


def myeven(begin, end):
    i = begin
    while i < end:
        if i % 2 == 0:  # 是偶数
            yield i
        i += 1

for x in myeven(1, 10):
    print(x)  # 打印 2, 4, 6, 8

L = [x**2 for x in myeven(4, 9)]
print(L)  # [16, 36, 64]
