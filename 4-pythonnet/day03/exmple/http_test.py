from socket import *

#创建套接字
s = socket()
s.bind(('0.0.0.0',8000))
s.listen(3)

c,addr = s.accept()#接受浏览器接受
print("Connect from",addr)
data = c.recv(4096)#浏览器发送请求
print(data)

#组织http响应
data = '''HTTP/1/1 200 OK
Content-Type:text/html

<h1>hello world</h1>
'''
c.send(data.encode())

c.close()
s.close()