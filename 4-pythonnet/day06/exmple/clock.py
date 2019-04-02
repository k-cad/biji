from multiprocessing import Process 
import time

#自定义类进程
class ClockProcess(Process):
    def __init__(self,value):
        super().__init__()
        self.value = value

    def f1(self):
        print('hello world')

    def f2(self):
        print('hello kitty')

    #重写run方法
    def run(self):
        for i in range(5):
            time.sleep(self.value)
            self.f1()
            self.f2()

# 创建进程对象
p = ClockProcess(2)
# 启动进程,执行run
p.start()
p.join()
