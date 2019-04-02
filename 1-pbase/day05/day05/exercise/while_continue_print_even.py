# 练习:
#   打印10以内的偶数(要求试用while语句+  continue)
#     采用跳过奇数的方式实现

x = 0
while x < 10:
    if x % 2 == 1:
        x += 1
        continue
    print(x)
    x += 1
