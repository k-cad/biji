#写一个生成器函数myeven(begin,end),用来生成从begin开始到end结束的所有偶数(不包含end)

def myeven(begin,end):
    i=begin
    while i<end:
        if i%2==0:
            yield i
        i+=1

for x in myeven(1,10):
    print(x)

L=[x**2 for x in myeven(4,9)]
print(L)