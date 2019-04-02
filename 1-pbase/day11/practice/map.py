# 1,求1**2+2**2+...+9**2的和
# 2,1**3+2**3+3**2+...+9**2的和
# 3,1**9+...9**1的和
def power2(x):
    return x**2
def power3(x):
    return x**3
# print(sum(map(power2,range(1,10))))
print(sum(map(lambda x:x**2,range(1,10))))
print('---------')
# print(sum(map(power3,range(1,10))))
print(sum(map(lambda x:x**3,range(1,10))))
print('---------')
print(sum(map(pow,range(1,10),range(9,0,-1))))