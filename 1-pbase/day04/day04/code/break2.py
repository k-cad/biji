#   2. 写程序,打印1~20的整数,打印在一行内
#       1 2 3 4 5 6 7 8 ...... 19 20
#   将以上内容打印20行

# break 语句只能终止当前循环语句的执行,如果有循环嵌套时,不
#        会跳出嵌套的外重循环

j = 1
while j <= 10:
    i = 1
    while i <= 20:
        print(i, end=' ', flush=True)
        if i == 15:
            break
        i += 1
    print()  # 换行print(sep=' ', end='\n', flush=False)
    j += 1




