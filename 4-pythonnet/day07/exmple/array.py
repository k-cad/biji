from multiprocessing import Process,Array
import time

shm = Array('i',[1,2,3,4,5])

def fun():
    for i in shm:
        print(i)

p = Process(target = fun)
p.start()
p.join()
