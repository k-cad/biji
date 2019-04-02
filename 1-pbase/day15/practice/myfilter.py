#写一个生成器函数 myfilter,要求此函数与系统内建函数filer 函数功能完全一致
 
def myfiltter(fn,iterable):
    for x in iterable:
        if fn(x):
            yield x



for y in myfiltter(lambda x: x%2==0,range(10)):
    print(y)