L=[1,3,7,5,2]
it = iter(L)
while True:
    try:
        x=next(it)
        print(x)
    except StopIteration:
        break