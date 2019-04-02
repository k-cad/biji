# 写程序算出1~20的阶乘的和，即1!+2!+...+20!

def myfac(n):
    if n==0:
        return 1
    else:
        return n*myfac(n-1)

n=int(input('请输入整数：'))

print(sum(map(myfac,range(1,n))))