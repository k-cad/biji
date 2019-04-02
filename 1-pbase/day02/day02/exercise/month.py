#   2. 输入一年中的月份(1~12)，输出这个月有哪儿个季度，如果输
#      入的是其它数，则提示: "您输错了"

month = int(input("请输入月份(1~12): "))

if 1 <= month <= 3:
    print("春季")
elif 4 <= month <= 6:
    print("夏季")
elif 7 <= month <= 9:
    print("秋季")
elif 10 <= month <= 12:
    print("冬季")
else:
    print("您输错了!!")
