# mymod.py

'''这是自定义模块mymod标题

此模块共有两个函数和两个数据如下:
.... 此处省略字
'''


# 此示例示意自定义一个mymod模块
def myfac(n):
    '''这是求阶乘的函数的文档字符串'''
    print("正在计算%d的阶乘" % n)

def mysum(n):
    print("正在计算1+2+3+...+%d的和" % n)

name1 = 'audi'
name2 = 'tesla'

print("mymod模块被加载")

print("mymod.py 模块内的__name__属性绑定的是:", __name__)



