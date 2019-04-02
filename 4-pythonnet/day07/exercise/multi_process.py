from test import *
import multiprocessing as mp
import time

jobs = []
t = time.time()
for i in range(10):
    # p = mp.Process(target=count,args=(1,1))
    p = mp.Process(target=myIO)
    p.start()
    jobs.append(i)
for i in jobs:
    p.join()

# print('Process CPU:',time.time()-t)
print('Process IO:',time.time()-t)
