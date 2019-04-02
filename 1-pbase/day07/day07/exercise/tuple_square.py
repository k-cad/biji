#   生成一个1~9的平方的元组,元组如下:
#     (1, 4, 9, 16, 25, ...., 81)

# 方法1
# t = ()
# for x in range(1, 10):
#     t += (x**2,)

# 方法2
# L = [x ** 2 for x in range(1, 10)]
# t = tuple(L)

# 方法3
# t = tuple(x**2 for x in range(1, 10))
# 等同于如下:
g = (x**2 for x in range(1, 10))
t = tuple(g)

print(t)
