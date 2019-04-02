# sequence_give_args.py


def myfun1(a,b,c):
    print(a)
    print(b)
    print(c)

L1=[1,2,3]
t2=(1,2,3)
s3='ABC'

myfun1(*L1)
myfun1(*t2)
myfun1(*s3)