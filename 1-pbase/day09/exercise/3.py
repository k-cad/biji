def myrange(start,stop=None,step=None):
    if stop is None:
        stop=start
        start=0
    if step is None:
        step=1
    if step>0:
        L=[]
        while start < stop:
            L.append(start)
            start += step
        return L
    elif step < 0:
        L=[]
        while start > stop:
            L.append(start)
            start += step[]
        return L
    

print(myrange(4))
print(myrange(2,10,3))
print(myrange(40,20,-2))