#求1/1+1/3+1/5+...+1/99的和


i=1
s=0
while i<=99:
    a=1/i
    s+=a
    i+=2
print(s)


