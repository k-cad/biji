#   1. 输入一个季度 1~4 输出这个季度有哪儿几个月,如果输入的
#   　　不是1~4的数，则提示用户"您输错了"


season = int(input("请输入季度(1~4): "))

if season == 1:
    print("春季有1,2,3月!")
elif season == 2:
    print("夏季有4,5,6月!")
elif season == 3:
    print("秋季有7,8,9月!")
elif season == 4:
    print("冬季有10,11,12月!")
else:
    print('您输错了!!!')

