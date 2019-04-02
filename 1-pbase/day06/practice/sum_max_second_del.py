L=[]
while True :
    x = int(input('请输入：'))
    if x <0:
        if len(L)<2:
            print('您输入的数太少了！')
            continue
        break
    
    if x not in L:
        L += [x]

print("和是",sum(L))
L1 = sorted(L)
print("最大的数",L1[-1])
print("第二大的数",L1[-2])
min_L=L1[0]
for i in range(len(L)):
    if L[i] == min_L:
        del L[i]
        break

print('删除最小的数后的列表是',L)


               

