a=1
b=2
c=3
def fn(c,d):
    e=300
    #此处有多少个局部变量
    print('locals()返回:',locals())
    #此处有多少个全局变量
    print('global()返回:',globals())
    print(globals['c'])

fn(100,200)