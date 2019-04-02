# 练习2
#   写一个函数print_even,传入一个参数n代表终止的整数,打印
#     0 ~ n 之间所有的偶数
#   如:
#     def print_even(n):
#         ..... 此处自己完成
#     print_even(10)
#   打印:
#     0
#     2
#     4
#     6
#     8


def print_even(n):
    for x in range(0, n+1, 2):
        print(x)

print_even(10)


