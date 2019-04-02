import sys
def myprint(*args,sep=' ',end='\n',file=sys.stdout,
            flush=False):
    flag = False
    # print(args)
    for x in args:
        if flag:
            file.write(sep)
        file.write(str(x))
        flag=True
    file.write(end)

print('hello world')
print(1,2,3,4)
print(5,6,7,8,sep='#')
print(1,2,3,4,sep=',')

    