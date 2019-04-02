s={'s','w','b','t'}
it=iter(s)
while True:
    try:
        x=next(it)
        print(x)
    except StopIteration:
        break