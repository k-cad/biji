# 算出100~999以内的水仙花数(Narcissistic number)
# 水仙花数是指百位

L=[]
for x in range(100,1000):

        a=x//100
        b=x%100//10
        c=x%10
        if a**3+b**3+c**3==x:
            L.append(x)

print(L)

