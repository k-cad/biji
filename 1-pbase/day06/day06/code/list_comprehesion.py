# 生成一个数值为1~9的整数的平方的列表,如:
#   L = [1, 4, 9, 16, 25, 36, 49, 64, 81]
# 用循环语句:
# L = []
# for x in range(1, 10):
#     L.append(x ** 2)

L = [x ** 2 for x in range(1, 10)]

print("L=", L)

