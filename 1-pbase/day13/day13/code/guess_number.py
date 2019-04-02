# guess_number.py

# 练习:
#   1. 猜数字游戏:
#     随机生成一个0~100之间的整数,用变量x绑定
#     让用户循环输入一个整数,用变量y绑定,输出猜数字的结果
#        如果y等于x,则提示'恭喜您猜对了',并结束猜数字
#        如果y大于x,则提示:'您猜大了'
#        如果y小于x,则提示:'您猜小了'

#     直到猜对为止,显示用户猜数字的次数后退出程序


import random   # 首先导入自己

x = random.randint(0, 100)  # x=random.randrange(101)

# print(x)

count = 0

while True:
    y = int(input("请输入整数: "))
    count += 1
    if y == x:
        print("恭喜您猜对了")
        break
    elif y > x:
        print("您猜大了")
    else:
        print("您猜小了")

print("您共猜了%d次" % count)