def myss(n):
    a=0
    for x in range(1,n+1):
        a += x**x
    return a

print(myss(3))

#法三
def mysum(n):
    s=sum([x])