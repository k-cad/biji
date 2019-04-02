# 练习:
#   已知有列表:
#     L = [1, 2, True, None, 3.14]
#     调用print函数,打印用'#'号分隔的文字信息到终端上
#   print(....)  # 打印  1#2#True#None#3.14



L = [1, 2, True, None, 3.14]

print(*L, sep="#")  # 打印  1#2#True#None#3.14
# 等同于print(1, 2, True, None, 3.14, sep='#')

