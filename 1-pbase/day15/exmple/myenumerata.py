def myenumerata(iterable,start= 0):
    for x in iterable:
        yield(start,x)
        start +=1
        




L=[3,5,8,10]
for i,v in myenumerata(L):
    print('索引为',i,'元素的值为：',v)
    