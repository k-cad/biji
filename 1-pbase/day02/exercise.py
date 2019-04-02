
s = input('请输入数字：')
x = int(s)
print("结果是:",x*2)

print(1,2,3,4) # 1 2 3 4
print(1, 2, 3, 4, sep=' ')
print(1, 2, 3, 4, sep='#')

print(1, 2, 3, 4, sep=' ', end='\n')
print(5, 6, 7, 8, end='')
print("AAAAAA",end='')

s = input('请输入第一个数字：')
x = int(s)
y = int(input('请输入第二个数字：'))
print('和为：',x + y)
print('积为：'，x * y)
 

x = int(input('请输入一个整数：'))
if x % 2 == 1:
    print(x,"是奇数")
else:
    print(x,"是偶数")

x = int(input('请输入一个整数：'))
if 50 <= x <= 100 :
    print(x,"在50与100之间")
else:
    print(x,"不在50~100之间")

if x < 0 :
    print("小于0")
else:
    print("不小于0")

x = int(input('请输入一个整数：'))
if 50 <= x <= 100 :
    print(x,"在50与100之间")
else:
    print(x,"不在50~100之间")

if x < 0 :
    print("小于0")
else:
    print("不小于0")

x = int(input('请输入一个数字：'))
if x > 0:
    print(x,'是正数')
elif x < 0:
    print(x,'是负数')
else:
    print(x,'是零')

season = int(input('请您输入季度(1~4)：'))
if season == 1:
    print("春季有一，二，三月")
elif season == 2:
    print("夏季有四，五，六月")
elif season == 3:
    print("秋季有七，八，九月")
elif season == 4:
    print('冬季有十，十一，十二月')
else:
    print('您输错了')


month = int(input('请您输入月份(1~12)：'))
if 1<=month<=3:
    print("春季")
elif month<=6:
    print('夏季')
elif month<=9:
    print('秋季')
elif month<=12:
    print('冬季')
else:
    print('您输错了')

month = int(input('请输入月份（１～１２）：'))
if 1<=month<=12:
    print('合法的月份')
    if month <=3:
        print('春季')
    elif month <= 6:
        print('夏季')
    elif month <= 9:
        print('秋季')
    else month <= 12:
        print('冬季')
else :
    print('您错了')


money = int(input('请输入商品总金额：'))

pay = money - 20 if money >= 100 else money 

print("需支付：",pay,"元")

x = int(input('请输入一个数：'))

if x < 0:
    result =-x 
else:
    result = x
print(x,'的绝对值：',result)

result = -x if x < 0 else x

