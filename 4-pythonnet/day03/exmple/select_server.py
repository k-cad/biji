from select import *
from socket import *

#创键套接字作为关注的IO
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',8000))
s.listen(5)

#添加关注列表
rlist = [s]
wlist = []
xlist = []

while True:
    #监控关注的IO
    rs,ws,xs = select(rlist,wlist,xlist)
    #遍历返回值列表,确定就绪的IO
    for r in rs:
        if r is s:
            c,addr = s.accept()
            print("Connect from",addr)
            #将客户端套接字加入关注
            rlist.append(c)
        #表示某个客户端发消息则C就绪
        else:
            data = r.recv(1024)
            if not data:
                rlist.remove(r)
                r.close()
                continue
            print("Receive:",data.encode())
            # r.send(b"Ok,Thanks")

            #当r放入wlist表示希望主动操作r这个IO
            wlist.append(r)

    for w in ws:
        w.send(b"OK,thanks")
        wlist.remove(w)
    
    for x in xs:
        pass

