# 练习:
#   任意输入一段字符串
#     1) 计算出这个字符串中空格的个数,并打印这个个数
#        (要求用for 语句,不允许使用S.count方法)
#     2) 计算出字符串中全部英文字母(A-Z和a-z)的个数,
#        并打印打印这个个数
#   完成上题后思考:
#     能否用while语句实现上述功能


s = input("请输入一段字符串: ")
blanks_count = 0
# 遍历输入的字符串,当有字符为' '时,将blanks_count做加1操作
for ch in s:
    if ch == ' ':
        blanks_count += 1
print("空格的个数是:", blanks_count)

# 2) 计算出字符串中全部英文字母(A-Z和a-z)的个数,
#    并打印打印这个个数
alpha_count = 0
for ch in s:
    # if 65 <= ord(ch) < 65+26 or 97 <= ord(ch) < 97+26:
    if 'A' <= ch <= 'Z' or 'a' <= ch <= 'z':
        alpha_count += 1
print("英文字母的个数是:", alpha_count)

#   完成上题后思考:
#     能否用while语句实现上述功能