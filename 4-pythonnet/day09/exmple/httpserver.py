# coding = uft-8
from socket import *
from threading import Thread
import sys

class HTTPServer(object):
    def __init__(self,server_addr,static_dir):
        self.server_addr = server_addr
        self.static_dir = static_dir
        self.create_socket()
        self.bind()

    def create_socket(self):
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

    def bind(self):
        self.sockfd.bind(self.server_addr)
        self.ip = self.server_addr[0]
        self.port = self.server_addr[1]

    def server_forever(self):
        self.sockfd.listen(5)
        print("Http server listen port %d" % self.port)
        while True:
            try:
                connfd,addr = self.sockfd.accept()
            except KeyboardInterrupt:
                self.sockfd.close()
                sys.exit('退出服务器')
            except Exception as e:
                print('Error',e)
                continue
            clientThread = Thread(target=self.handle,args=(connfd,))
            clientThread.setDaemon(True)
            clientThread.start()

    def handle(self,connfd):
        #接受http请求
        request = connfd.recv(4096)
        if not request:
            connfd.close()
            return

        requestlines = request.splitlines()
        print(connfd.getpeername(),':',requestlines[0])

        getRequest = str(requestlines[0]).split(' ')[1]
        if getRequest == '/' or getRequest[-5:] == '.html':
            self.get_html(conffd,getRequest)
        else:
            self.get_data()

    def get_html(conffd,getRequest):
        if getRequest == '/':
            filename = self.static_dir + '/index.html'
        else:
            filename = self.static_dir + getRequest
        try:
            f =open(filename)
        except IOError:
            responseHeadlers = 'HttP/1.1 404 Not Foud\r\n'

    def get_data(self,connfd.getRequest):
        responseHeadlers = "HTTP/1.1 200 OK\r\n"
        responseHeadlers += "\r\n"
        responseBody = '<h1>Wating httpserver 3.0<h1>'




if __name__ == "__main__":
    #用户自己设定的内容
    server_addr = ('0.0.0.0',8888)
    #用户提供自己要展示的网页
    static_dir = './static'

    httpd = HTTPServer(server_addr,static_dir)

    httpd.server_forever()
















