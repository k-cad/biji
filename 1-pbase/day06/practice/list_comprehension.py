# 生成一个数值为1~9的整数的平方和的列表，如：
# L = [1,4,9,25,36,49,64,81]
# L =[x**2 for x in range(1,10)]
# print('L=',L)

#练习：用列表推导式生成1~100内的所有奇数的列表

# L = [x for x in range(1,100,2)]
# print('L=',L)


L = [x for x in range(1,100,2) if x%2==1]
print('L=',L)

