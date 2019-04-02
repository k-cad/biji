#   2. 已知有两个字符串列表:
#     Nos = [1001, 1002, 1005, 1008]
#     names = ['Tom', 'Jerry', 'Spike', 'Tyke']

#     生成以Nos 中项为键，以names中的项为值的字典
#     d = {1001: 'Tom', 1002:'Jerry', ....}



Nos = [1001, 1002, 1005, 1008]
names = ['Tom', 'Jerry', 'Spike', 'Tyke']

# d = {}
# for n in Nos:
#     d[n] = names[Nos.index(n)]

d = {n: names[Nos.index(n)] for n in Nos}

print(d)




