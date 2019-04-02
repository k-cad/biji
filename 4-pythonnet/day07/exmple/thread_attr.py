from threading import Thread
from time import sleep

def fun():
    sleep(3)
    print("线程属性测试")

t = Thread(target=fun,name="mars")


# 线程
t.setName('brostone')
print('Thread name:',t.name)
print("Thread name:",t.getName())

#设置daemon为True
t.setDaemon(True)
t.start()
# 查看线程周期
print('alive:',t.is_alive())

# t.join()
