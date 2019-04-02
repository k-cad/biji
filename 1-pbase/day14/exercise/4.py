def ta(n):
    
    ls=[1]
    L=[ls]

    for i in range(2,n+1):
        l=[]
        for j in range(i):
            if j==0 or j==i-1:
                l.append(1)
            else:
                x=int(ls[j]+ls[j-1])
                l.append(x)
        ls=l
        L.append(ls)
    return L
def get_yangui_string_list(L):
    '''此函数 传入一个由数字列表组成的列表，返回字符串列表
    如: L = [[1], [1, 1], [1, 2, 1]]
    返回 ['1', '1 1', '1 2 1']'''

    L2 = []  # 准备存放字符串
    for layer in L:
        s = ' '.join((str(x) for x in layer))
        L2.append(s)
    return L2

def print_yanghui_triangle(L):
    max_len = len(L[-1])
    for s in L:
        print(s.center(max_len))

L = ta(10)  # 得到六层数据
string_L = get_yangui_string_list(L)
print_yanghui_triangle(string_L)