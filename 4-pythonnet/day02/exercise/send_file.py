from socket import *

s = socket()
s.connect(('127.0.0.1',8000))

f = open('Jenyfa Duncan - Australia.ogg','rb')

while True:
    data = f.read(1024)
    if not data:
        break
    s.send(data)

f.close()
s.close()