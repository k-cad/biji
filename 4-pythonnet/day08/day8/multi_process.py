from test import *
import multiprocessing as mp
import time 

def io():
    write()
    read()

jobs = []
t = time.time()
for i in range(10):
    p = mp.Process(target=io)
    p.start()
    jobs.append(p)
for i in jobs:
    i.join()
print("Process cpu:",time.time()-t)
