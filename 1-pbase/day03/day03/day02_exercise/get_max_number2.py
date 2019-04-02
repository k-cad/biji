#   2. 写程序,任意给出三个数,打印出三个数中最大的一个数

a = int(input("请输入第1个数: "))
b = int(input("请输入第2个数: "))
c = int(input("请输入第3个数: "))

# 改进算法:
# 先假设第一个最大,用变量绑定
zuida = a
if b > zuida:
    zuida = b

if c > zuida:
    zuida = c

print("最大数是:", zuida)


# if a > b:
#     # a 和 c 再比
#     if a > c:
#         print("最大数是", a)
#     else:
#         print("最大数是", c)
# else:
#     # b 和 c 再比
#     if b > c:
#         print("最大数是", b)
#     else:
#         print("最大数是", c)

