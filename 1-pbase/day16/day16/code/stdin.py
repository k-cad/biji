

import sys

# s = input("请输入")  # 内部就是调用sys.stdin
print("请输入内容:")
s = sys.stdin.readline() 
print(s)
print(len(s))  # 算'\n'在内

s = sys.stdin.read()  # ctrl + d 结束
print(s)