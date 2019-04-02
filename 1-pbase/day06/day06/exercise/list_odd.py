# 练习 :
#   用列表推导式生成 1~100 内所有奇数组成的列表
#   结果是:[1, 3, 5, 7, ....., 99]

# L = [x for x in range(1, 100, 2)]
L = [x for x in range(1, 100) if x % 2 == 1]
print(L)

L = []
for x in range(1, 100):
    if x % 2 == 1:
        L.append(x)
print("L=", L)