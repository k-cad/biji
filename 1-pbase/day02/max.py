a=int(input('第一个：'))
b=int(input('第二个：'))
c=int(input('第三个：'))
# if a>=b and a>=c:
#     print("最值",a)
# elif b>=c and b>=a:
#     print('最值',b)
# else:
#     print('最值',c)
m = a
if b > m:
    b = m
if c>m:
    m=c
print(m)
