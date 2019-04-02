n=int(input('输入：'))
s=0
i=1
# while i <= n:
#     if i % 2 == 1:
#         a = 1/(2*n-1)
#     if i % 2 == 0:
#         a = -1/(2*n-1)
#     s += a 
#     i += 1

# print(4*s)
while i <= n:
    a= 1/(2*i-1)
    s+=a
    i += 1
    a=-1/(2*i-1)
    s+=a
    i+=1
print(s)
print(4*s)
    

