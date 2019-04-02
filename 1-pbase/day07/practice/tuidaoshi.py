# 练习
# 　有如下列表
# 　　　　　　L = ['tarena','xiao','hello']
#   生成{'hello': 5, 'tarena': 6, 'xiao': 4}
# L = ['tarena','xiao','hello']
# d = {x:len(x) for x in L}
# print(d)
 


Nos=[1001,1002,1003,1008]
names=['tom','Jerry','spk','tyke']
#法一
# d={}
# for i in range(len(Nos)):
#     d[Nos[i]]=names[i]
# 法二
d={Nos[i]:names[i] for i in range(len(Nos))}
＃　法三
d={n:names[Nos.index(n)] for n in Nos}
print(d)


