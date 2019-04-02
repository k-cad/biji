# 练习：写一个程序，输入一个字符串，统计出这个字符串的字符种类及个数
# d={}
# i=0
# while True:
#     k = input('请输入：')
#     if k in d:
#         i += 1
#         d.update({k:i})
#     if k not True:
#         break

# for k,v in d.items():
#     print('字符Ａ：',k,v,'次')
s = input('请输入：')
d={}

for k in s:
    if k not in d:
        d[k]=1
    else:
        d[k] += 1
for k in d:
    print(k,d[k])
         
