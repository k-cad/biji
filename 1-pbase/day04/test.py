# 练习
# 1,打印1~20的整数
# 2,写程序，打印1~20的整数，打印在一行内
# 1 2 3 4 5 6 ... 20
# 3,写程序，打印1~20的整数，每行五个，打印四行，如：
# 1 2 3 4 5
# 6 7 8 9 10
# 11 12 ...
# 可以if 语句嵌入到while语句中
# 第一题
# i = 1
# while i <= 20:
#     print(i)
#     i += 1
# 第二题
j = 1
while j <= 10:
    i=1
    while i<= 20:
        print(i,end=' ')
        i += 1
    print()
    j += 1
#第三题
# i=1
# while i<=20:
#     print(i,end=' ')
#     if i % 5==0:
#         print()
#     i += 1
# print()
#　写一个程序，输入一个开始的整数存于begin变量中
#　输入结束的整数存于end变量中
# 打印从begin到end的每个数　
# 打印在一行
# begin = int(input('请输入：'))
# end = int(input('请输入：'))
# count = 0 #打印计数量
# i = begin
# while i < end:
#     print(i,end=' ')
#     count += 1
#     if count % 5 == 0:
#         print()
#     i += 1
# print()




