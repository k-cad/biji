L=[]
while True:
    x = int(input('请输入：'))
    if x == -1:
        break
    L += [x]
print(L)
print(max(L))
print(min(L))
print(len(L))
print(sum(L)/len(L)) 