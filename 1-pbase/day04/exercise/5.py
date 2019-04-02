
#第一次循环控制行数
y=1
while y<= 9:
    #此处打印每行的y个乘法
    x=1
    while x<=y:
        print('%d*%d=%-2d'% (x,y,x*y),end=' ')
        x += 1
    print()
    y += 1
