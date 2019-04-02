# def say_hello():
#     print('hello world')
#     print('hello China')
#     return 1+2
#     print('hello python')
# v=say_hello()
# print('v=',v)
#练习： 1，写一个函数mymax,实现返回两个数的最大值
# def my_max(a,b):
#     return max(a,b)
# print(my_max(100,200))


# 2,写一个函数myadd,实现给出两个数，返回两个数的和
# def myadd(x,y):
#     return x+y
# a=int(input('第一个数'))
# b=int(input('第二个数'))
# print(myadd(a,b))


# 3,写一个函数 input_number
def input_number():
    L1=[]
    while True:
        n=int(input('请输入：'))
        if n<0:
            break
        L1.append(n)
    return L1
L = input_number()
print(L)
print(max(L))
        
