# 练习:
#   1. 写一个函数mymax, 实现返回两个数的最大值:
#     如:
#       def mymax(a, b):
#           .... # 此处自己实现

#       print(mymax(100, 200))  # 200
#       print(mymax("ABC", 'ABCD'))  # ABCD

# 方法1
# def mymax(a, b):
#     zuida = a
#     if b > zuida:
#         zuida = b
#     return zuida

# 方法2
# def mymax(a, b):
#     if a > b:
#         return a
#     else:
#         return b

# 方法3
def mymax(a, b):
    if a > b:
        return a
    return b

print(mymax(100, 200))  # 200
print(mymax("ABC", 'ABCD'))  # ABCD

