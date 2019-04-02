#练习：
#    输入一个整数，打印正方形
#    1 2 3 4 5
#    1 2 3 4 5
#    1 2 3 4 5
#    1 2 3 4 5
#    1 2 3 4 5
n = int(input('输入一个数：'))
for x in range(1,n+1):
    for x in range (x,x+5):
        print(x,end=" ")
        x += 1
    print()
