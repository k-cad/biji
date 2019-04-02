# def myfac(n):
#     a=1
#     for x in range(1,n+1):
#         a *= x
#     return a

# print(myfac(5))
def myfac(n):
    if n==0:
        return 1
    else:
        return n*myfac(n-1)#n!=n*(n-1)!
print(myfac(5))