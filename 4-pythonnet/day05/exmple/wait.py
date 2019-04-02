import os
from time import sleep

pid = os.fork()

if pid < 0:
    print('Error')
elif pid == 0:
    sleep(2)
    print("Child %d Process exit" % os.getpid())
    os._exit(2)
else:
    pid,status = os.wait()
    print("pid:",pid)
    print("status",status)
    while True:
        pass
