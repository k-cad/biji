import os
from time import sleep

pid = os.fork()

if pid < 0:
    print('Error')
elif pid == 0:
    sleep(2)
    print("Child %d Process exit" % os.getpid())
    os._exit(3)
else:
    # 非阻塞
    while True:
        sleep(1)
        p,status = os.waitpid(-1,os.WNOHANG)
        if p != 0:
            break
        print("Something else")
    print('p = ',p)
    print("status=",status)