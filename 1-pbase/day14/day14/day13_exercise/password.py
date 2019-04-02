#   1. 随机生成6位密码:
#       可以作为密码的字符有:
#         a-z, A-Z, 0-9
#     随机生成一个6位的密码

import random

charator = [chr(x) for x in range(65, 65+26)]
charator += [chr(x) for x in range(97, 97+26)]
charator += [str(x) for x in range(10)]

# print(charator)
passwd = ''
for _ in range(6):
    passwd += random.choice(charator)

print("密码是:", passwd)

