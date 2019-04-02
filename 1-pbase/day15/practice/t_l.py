L=[2,3,5,7]
a=[x*10 for x in L]#容器
it=iter(a)
print(next(it))
L[1]=33
print(next(it))

L=[2,3,5,7]
a=(x*10 for x in L)#生成器
it=iter(a)
print(next(it))
L[1]=33
print(next(it))