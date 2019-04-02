import re
f = open('./test.py')
data = f.read()

pattern1 = r'\b[A-Z]\S*?\b'

pattern2 = r'-?\d+\.?/?\d*%?'

pattern3 = r'\d{4}-\d{1,2}-\d{1,2}'

# regex = re.compile(pattern2)
regex = re.compile(pattern3)

# for i in regex.finditer(data):
#     print(i.group())
for i in regex.finditer(data):
    s = i.group()
    print(re.sub(r'-','.',s))
f.close()




# w = re.findall(r'^[A-Z]\w*',s)
# d = re.findall(r'\d+|\d+.\d+',s)
# d = re.findall(r'-(\d+|\d+.\d+)',s)
# d = re.findall(r'(\d+|\d+.\d+)%',s)
# d = re.findall(r'\d+/\d+',s)
# date = re.findall(r'-',.,s)



