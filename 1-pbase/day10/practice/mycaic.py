# 练习：
#     写一个计算公式的解释执行器
#         已知有如下一些函数：
#         def  myadd(x,y):
#             return x+y
#         def  mysum(x,y):
#             return x-y
#         def mymul(x,y):
#             return x*y
#         ...
#         定一个带有一个参数的函数 get_func(s):
#             def get_func(s):
#                 ... 
#     此函数在传入字符串'加'或'+'返回myadd函数；
#     在函数在传入字符串
#主程序如下
#     def main():
#          while True:#         
#             s=input('请输入公式：')
#             L=s.split()
#             a=int(L[0])
#             b=int(L[2])
#             fn = get_func(L[1])
#             print('结果是：',fn(a,b))


def  myadd(x,y):
    return x+y
def  mysum(x,y):
    return x-y
def mymul(x,y):
    return x*y
def get_func(s):
    # def  myadd(x,y):
    #     return x+y
    # def  mysum(x,y):
    #     return x-y
    # def mymul(x,y):
        return x*y
    if s=='+' or s=='加':
        return myadd
    if s=='-' or s=='减':
        return mysum
    if s=='*' or s=='乘':
        return mymul
def main():
    while True:
        s=input('请输入公式：')
        L=s.split()
        a=int(L[0])
        b=int(L[2])
        fn = get_func(L[1])
        print('结果是：',fn(a,b))

main()