# 创建二级子进程处理僵尸

import os
from time import sleep

def f1():
    sleep(3)
    print('doing...')

def f2():
    sleep(4):
    print("doing another")

pid = os.fork()

if pid < 0:
    print("Error")
elif pid == 0:
    p = os.fork()#创建二级子进程
    if p == 0:
        f2()
    else:
        os._exit(0)#一级子进程退出
else:
    os.wait()#等一级子进程退出
    f1()
















