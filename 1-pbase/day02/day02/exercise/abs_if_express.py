#   2. 写一个程序,输入一个数,用条件表达式计算这个数的绝对值,
#      并打印此绝对值

x = int(input("请输入一个数: "))

result = -x if x < 0 else x

print(x, '的绝对值是:', result)