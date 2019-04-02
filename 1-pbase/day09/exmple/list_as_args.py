# list_as_args.py
# 此示例示意,当函数的参数为可变数据类型时，在函数内部可以改为容器的内容

L=[1,2,3,4]
t=(1.1,2.2,3.3,4.4)
 
def append_5(x):
    # x.append(5)
    x += 5
    print('x=',x)#1.1,2.2,3.3,4.4,5

append_5(L)
print(L) # 1,2,3,4,5
append_5(t)
print(t)#1.1,2.2,3.3,4.4


#写一个函数此函数读取用户输入的数据，最后保存于全局变量的列表L中，当用户输入小于零的数时结束输入
L=[]
def input_number(L1):
    while True:
        x=int(input('请输入：'))
        if x < 0:
            break
            L1.append(x)
input_number(L)
print(L)
input_number(L)
print(L)
