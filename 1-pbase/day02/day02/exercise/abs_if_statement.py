#   1. 写一个程序,输入一个数,用if语句计算这个数的绝对值,并打
#      印此绝对值

x = int(input("请输入一个数: "))

# 方法1
# if x < 0:
#     result = -x  # 用result来记录结果
# else:
#     result = x

# 方法2
result = x
if result < 0:
    result = -result  # 符号取反


print(x, '的绝对值是:', result)