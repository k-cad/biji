
import random as r
y=r.randint(0,100)#随机生成1~100之间的数用y绑定
count=0
while True:
    x=int(input('请输入'))#让用户循环输入一个整数，用x绑定
    count += 1
    if x>y:
        print('大了')
    elif x<y:
        print('小了')
    elif x==y:
        print('对了')
        break
print('猜了%d次' % count)

