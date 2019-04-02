'''
http server v1.0
接收浏览器的请求
返回固定的相应内容
'''
from socket import *
#处理客户端请求
def handleCilent(connfd):
    print("Request from",connfd.getpeername())
    request = connfd.recv(4096)
    #将request按行分割
    request_line = request.splitlines()
    for line in request_line:
        print(line)
    try:
        f =open('index.html')
    except IOError:
        response = "HTTP/1.1 404 Not Found\r\n"
        response += "\r\n"
        response += "====Sorry not found===="
    else:
        response = "HTTP/1.1 200 OK\r\n"
        response += '\r\n'
        response += f.read()
    finally:
        connfd.send(response.encode())
#创建套接字TCP
def main():
    sockfd = socket()
    sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    sockfd.bind(('0.0.0.0',8000))
    sockfd.listen(3)
    print("Listen to the port 8000")
    while True:
        connfd,addr = sockfd.accept()
        handleCilent(connfd) #负责具体请求处理
        connfd.close()

if __name__ == "__main__":
    main()

















