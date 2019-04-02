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
alpha_count = 0
i = 0  # i 代表字符串的索引
while i < len(s):  # 索引不允许大于等于len(s)
    ch = s[i]  # ch绑定每次遍历的字符
    # 统计个数
    if ch == ' ':
        blanks_count += 1
    if 'A' <= ch <= 'Z' or 'a' <= ch <= 'z':
        alpha_count += 1
    i += 1  # 索引增加1,

print("空格的个数是:", blanks_count)
print("英文字母的个数是:", alpha_count)

