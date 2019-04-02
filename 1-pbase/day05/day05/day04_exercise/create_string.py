#   2. 写程序用while 语句生成如下的字符串,并打印出来
#      1) 'ABCD........XYZ'
#      2) 'AaBbCcDd..........XxYyZz'

s = ''  # 此字符串用来累加大写字符
code = ord('A')   # code = 65
while code < ord('A') + 26:
    ch = chr(code)  # 用当前编码转为字母
    s += ch  # 把生成的字母累加到s中
    code += 1
print("s=", s)

s2 = ''  # 此字符串用来累加大写小写字符
code = ord('A')   # code = 65
while code < ord('A') + 26:
    ch = chr(code)  # 用当前编码转为大写字母
    s2 += ch  # 把生成的大写字母累加到s2中
    ch = chr(code + 32)  # 生成小写字母
    s2 += ch
    code += 1
print("s2=", s2)


