def power2(x):
    print('power2被调用！x=',x)
    return x**2

for x in map (power2,range(1,10)):
    print(x)

print(sum(map(powe2,range(1,10))))