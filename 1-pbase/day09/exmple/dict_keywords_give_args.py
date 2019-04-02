# dict_keywords_give_args.py


def myfun1(a,b,c):
    print(a)
    print(b)
    print(c)

d1={'c':33,'a':11,'b':22}

myfun1(c=d1['c'],b=d1['b'],a=d1['a'])
myfun1(**d1)
