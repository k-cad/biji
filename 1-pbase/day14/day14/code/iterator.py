# iterator.py


L = [2, 3, 5, 7]
# 如何遍历L中数据
# 方法1
# i = 0
# while i < len(L):
#     x = L[i]
#     print(x)
#     i += 1

# 方法2
# for x in L:
#     print(x)

# 方法3 用迭代器来遍历
it = iter(L)
while True:
    try:
        x = next(it)
        print(x)
    except StopIteration:
        break

