# L=['Jerry','Tom','Spike','Tyke']
# l=[]
# for x in L:
#     y=x[::-1]
#     l.append(y)
# L1=sorted(l)
# print(L1)

def reverse_str(s):
    r=s[::-1]
    return r

names=['Jerry','Tom','Spike','Tyke']
L=sorted(names,key=reverse_str)
print(L)