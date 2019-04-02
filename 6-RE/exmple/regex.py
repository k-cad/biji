import re

s ="zhang:1994 Li:1995"
pattern = r'(\w+):(\d+)'

# l = re.findall(pattern,s)
# print(l)

regex = re.compile(pattern)
l = regex.findall(s,0,10)
print(l)

l = re.split(r'\s+','Hello     world')
print(l)

s = re.sub(r'傻逼','**','基于,傻逼,傻逼,傻逼',2)
print(s)

s = re.subn(r'傻逼','**','基于,傻逼,傻逼,傻逼',2)
print(s)




















