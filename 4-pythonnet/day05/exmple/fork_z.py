import os
from time import sleep

pid = os.fork()

if pid == 0:
    print("Child PID:",os.getpgid())
    sys.exit("子进程结束")
else:
    while True:
        sleep(2)
        print('bye')
        