# raise.py

def make_except():
    print('函数开始 ')
    # int('aaa')
    error = ValueError('故意制造的错误')
    raise error
    print('函数结束')

try:
    make_except()
    print('make_except 调用完毕')
except ZeroDivisionError:
    print('make_except 函数调用发生异常')
except ValueError as err:
    print('发生了值错误')
    print('发生错误的数据是：',err)
print('程序正常退出')
