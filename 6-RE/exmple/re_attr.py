import re
regex = re.compile(r'w+',flags=re.A)
# regex = re.compile(r'.+',flags=re.S)
# regex = re.compile(r'^达内',flags=re.M)

s = '''Welcome to
达内
'''

l = regex.findall(s)
print(l)