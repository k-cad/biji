import re
s = "2018年4月28号"

pattern = r'\d+'

it = re.finditer(pattern,s)

for i in it:
    print(i.group())



obj = re.fullmatch(r'\w+','hello world')
print(obj.group())

obj = re.match(r'[A-Z]\w+','Hello World')
print(obj.group())

obj = re.search(r'\d+',"Today 2018-1-18")