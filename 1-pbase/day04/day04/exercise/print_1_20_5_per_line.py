#   3. 写程序,打印1~20的整数,每行五个,打印四行,如:
#       1 2 3 4 5
#       6 7 8 9 10
#       11 12 ...
#       ...
#     提示:  可以将if语句嵌入到while语句中

i = 1
while i <= 20:
    print(i, end=' ', flush=True)
    if i % 5 == 0:
        print()  # 换行
    # if i == 5:
    #     print()
    # elif i == 10:
    #     print()
    # elif i == 15:
    #     print()
    # elif i == 20:
    #     print()
    i += 1

