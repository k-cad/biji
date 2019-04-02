#写一个函数myadd,此函数可以计算两个数，三个数及四个数的和
def myadd(a,b,c=0,d=0):
    s=sum([a,b,c],d)
    
    return s

print(myadd(10,20))
print(myadd(100,200,300))
print(myadd(1,2,3,4))