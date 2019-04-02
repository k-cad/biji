# if_elif_else.py


# 输入一个整数,让程序来打印出这个数是 正数,零,负数

x = int(input("请输入一个数字: "))
if x > 0:
    print(x, '是正数')
elif x < 0:
    print(x, '是负数')
else:
    print(x, '是零')



