#已知有列表L=[2,3,5,7]
#1,写一个生成器函数，让此函数能够动态提供数据,数据为原列表的数字平方加一
#2,写一个生成器表达式，让此函数能够动态提供数据,数据为原列表的数字平方加一
#3,创建一个列表，此列表内的数据为原列表的数字平方加一

def fun(lst):
    for x in L:
        yield x**2+1

L=[2,3,5,7]
for x in fun(L):
    print(x)



for a in (x**2+1 for x in L):
    print(a)

L=[x**2+1 for x in L]
print(L)

