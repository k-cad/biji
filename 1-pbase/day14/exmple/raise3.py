# raise3.py 此示例示意用raise 无参调用来传递信息

def f1():
    print('f1开始...')
    raise ValueError('f1内部发生错误!')
    print('f1结束!!!')

def f2():
    try:
        f1()
    except ValueError as e:
        print('f2中收到f1发生的错误：',e)
        raise #raise e
try:
     f2()
except ValueError as err:
    print('主程序中已收到f2中发生的错误：',err)
