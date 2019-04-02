from socket import *
from multiprocessing import Process 

HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST,PORT)

def handle(c):
    print("Connect from",c.getpeername())
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send('OK')
    c.close()

s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(ADDR)
s.listen(5)

#处理僵尸进程
signal.signal(sign)
while True:
    try:
        c,addr = s.accept()
    except KeyboardInterrupt:
        s.close()
        break
    except Exception as e:
        print(e)
        continue
    
    #创建进程处理客户端请求
    p = Process(target=handle,args=(c,))
    p.daemon = True#子进程父进程退出
    p.start()
    