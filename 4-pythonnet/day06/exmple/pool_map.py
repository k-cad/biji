from multiprocessing import Pool 
from time import sleep,ctime

#进程事件
def fun(n):
    sleep(2)
    return n*n

# 创建进程池
pool = Pool()

r = pool.map(fun,[1,2,3,4,5])
    
# 关闭进程池
pool.close()
# 回收进程池
pool.join()

print(r)