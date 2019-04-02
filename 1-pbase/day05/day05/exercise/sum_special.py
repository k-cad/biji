#   2. 求 1 ~ 100 之间所有不能被2, 3, 5 和 7 中任意一个数
#      整除的数的和(用continue实现)
s = 0  # 用于累加和
for x in range(1, 101):
    if x % 2 == 0:
        continue
    if x % 3 == 0:
        continue
    if x % 5 == 0:
        continue
    if x % 7 == 0:
        continue
    # print(x)
    s += x

print("最终的和是:", s)