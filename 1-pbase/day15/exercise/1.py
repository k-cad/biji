def myrange(*args):
    if len(*args)==1:
        step=1
        start=0
        end=args[0]
    elif len(*args)==2:
        step=1
        start=args[0]
        end=args[1]
    elif len(*args)==3:
        step=[2]
        start=args[0]
        end=args[1]
    if step > 0:
        while start < end:
            yield start
            start+=step
        raise StopIteration
    elif step <0:
        while start > end:
            yield start
            start +=step
        raise StopIteration
    else:
        raise('stop cannot be 0')


print(x**2 for x in myrange(1,18,3))