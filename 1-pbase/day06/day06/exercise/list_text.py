# 练习:
#   输入多行文字,存入列表中
#   每次输入后回车算作一行,任意输入多行文字.
#   当直接输入回车(即空行时算作输入结束)
#     要求:
#       1) 按原输入的内容在屏幕上输出内容
#       2) 打印出您共输入了多少行文字
#       3) 打印出您共输入了多少个字符
#     如:
#       请输入: ABC 
#       请输入: abc
#       请输入: 123
#       请输入: <回车>
#     您输入的内容是:
#       ABC
#       abc
#       123
#     您输入了3行文字
#     您输入了9个字符


L = []

while True:
    s = input("请输入: ")
    if not s:  #  当输用户直接输入回车时,得到空字符串
        break
    L.append(s)  # 将字符串s追加到L列表末尾
print("L=", L)
print("您输入的内容是:")
for text in L:
    print(text)

print("您输入了", len(L), '行文字')

count = 0
for text in L:
    count += len(text)  # 把每一行字符串长度累加到count中
print("您输入了", count, '个字符')
