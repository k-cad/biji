from socket import *


s = socket()
s.bind(('127.0.0.1',8000))
s.listen(3)

c,addr = s.accept()
print("Connect from",addr)

f = open('Jenyfa Duncan.ogg','wb')

while True:
    data = c.recv(1024)
    if not data:
        break
    f.write(data)
f.close()
c.close()
s.close()





