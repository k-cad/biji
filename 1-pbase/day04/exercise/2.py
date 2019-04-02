#写程序用while打印
# 'ABCD...XYZ'
# 'AaBbCcDd...Zz'
# s1=''
# code = ord('A')
# while code < ord('A')+26:
#     ch = chr(code)
#     s1 += ch
#     code += 1
# print(s1)

# ord('A')-ord('a')=32
s2=''
code = ord('A')
while code < ord('A')+26:
    ch = chr(code)
    s2 += ch
    ch = chr(code+32)
    s2 += ch
    code += 1
print(s2)

