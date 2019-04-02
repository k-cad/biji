L=[1,2,3]
v=100
def f1():
    L.append(4)
    v=200
f()
print(L)
print(v)

def f2():
    L.append([5])
    # L+=[5] 出错
    # v+=1  出错
f2()

print(L)
print(v)
