# 生成前40个斐波那契数(Fibonacci)
#     1 1 2 3 5  8 13 21
# 要求：将这些书保留在列表中，最后打印这些数
L=[]
a=0#表示第一个数的前一位
b=1#表示第一个数

while len(L) <= 40:
    L.append(b)#每次把b加入列表
    c = a + b # a,b=b,a+b
    a=b
    b=c
    
    print(L)

# L=[1,1]
# while len[L]<40:
#     L.append(L[-1]+L[-2])
     


