# list_as_args2.py


# 写一个函数,此函数读取用户输入的数据,最后保存于全局变量的列表
# L中, 当用户输入小于零的数时结束输入
L = []
def input_number(L1):
    while True:
        x = int(input('请输入:'))
        if x < 0:
            break
        L1.append(x)

input_number(L)
print(L)
input_number(L)
print(L)






