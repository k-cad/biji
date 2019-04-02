# 练习:
#   写一个程序,输入三行文字,让这三行文字依次以20个字符的宽度
#   右对齐输出
#   如:
#     请输入第1行: hello china
#     请输入第2行: tanena
#     请输入第3行: a
#   打印如下:
#              hello china
#                   tanena
#                        a

#   做完上题后再思考:
#     能否以最长的字符串长度进行右对齐显示(左侧填充空格)

a = input('请输入第1行: ')
b = input('请输入第2行: ')
c = input('请输入第3行: ')

# 求三个字符串的最大长度
max_len = len(a)
if len(b) > max_len:
    max_len = len(b)
if len(c) > max_len:
    max_len = len(c)

# print('最长的字符串长度是:', max_len)
# 方法1,左侧手动添加空格
# print(' ' * (max_len-len(a)) + a)
# print(' ' * (max_len-len(b)) + b)
# print(' ' * (max_len-len(c)) + c)

# 方法2,根据最长的字符串长度max_len 来生成相应的格式化字符串
# 如 max_len 绑定10 ,则生成 '%10s'

fmt = "%" + str(max_len) +"s"
# print("fmt=", fmt)

print(fmt % a)
print(fmt % b)
print(fmt % c)
