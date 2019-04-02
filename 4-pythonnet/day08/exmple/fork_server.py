from socket import *
import os,sys
import signal

def client_handle(c):
    print("客户端:",c.getpeername())
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b'Receive message')
        c.close()
        
#创建套接字
HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST.PORT)

s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(ADDR)
s.listen(5)

# 处理僵尸进程
signal.signal(signal.SIGCHLD,signal.SIG_IGN)

print("listen to the port 888...")
# 循环等待客户端连接
while True:
    try:
        c.addr = s.accept()
    except KeyboardInterrupt:
        s.close()
        sys.exit("服务器退出")
    except Exception as e:
        print('ERROR:',e)
        continue
    #创建子进程处理客户端
    pid = os.fork()

    if pid = 0:
        client_handle()
        os._exit(0)
    else:
        pass

