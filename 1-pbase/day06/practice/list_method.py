#输入多行文字，存入列表中　
# 每次输入后回车算作一行，任意输入多行文字
# 当直接输入回车时(即空行时算作结束)
#要求
#   1)按原输入的内容在屏幕输出
#   2)

L = []
while True:
    s = input('请输入：')
    if not s:
        break
    L.append(s)
print('L:',L)
print('您输入的内容是：')
for text in L:
    print(text)

print('您输入了',len(text),'行')
print('您输入了',len(L),'字')