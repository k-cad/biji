# 有一些数存于列表中　如：L=[1,3,2,1,6,4,2,......,98,82]
# 1)将列表出现的数字存入另一个列表L2中，要求：重复出现多次的数在L2中保留一份
# 2)将列表中出现两次的数字存在L3列表中，在L3列表中只保留一份

L=[]
while True:
    x = input('请输入：')
    if x == '':
        break
    L += [int(x)]
        

print(L)

# L1=[1,2,3,2,2,34,3,2,1,6,4,3,2,98,82,2]
# L2=[]
# for i in L1:
# L3=[]
#     if i not in L2:
#         L2.append(i)
# print(L2)


# for i in L1:
#     if i  not in L3 and L1.count(i)==2:
#         L3.append(i)
# print(L3)
    
