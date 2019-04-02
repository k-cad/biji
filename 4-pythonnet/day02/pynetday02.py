回顾
1.OSI七层模型 TCP/IP模型
2.三次握手 四次挥手
3.TCP 和 UDP 
4.网络概念:网络主机 端口 IP地址 域名
5.套接字编程:网络编程技术手段
        流式套接字:TCP 
        数据报套接字: UDP
6.TCP套接字流程
    服务端:socket()-->bind()-->listen()-->accept()
        -->recv(),send()-->close()
    客户端:socket()-->connect()-->send(),recv()-->close()

笔记
一.TCP套接字数据传输特点
    *TCP连接中当有一端退出,另一端如果阻塞在recv,
    此时recv会立即返回一个空字节串
    *TCP连接中如果一段已经不存在,仍然试图通过send发送
    则会产生BrokenPipeError
    *一个监听套接字可以同时连接多个客户端,也能够重复被连接
    *收发缓冲区
        【1】网络缓冲区有效的协调了消息的收发速度
        【2】send和recv
        实际是向缓冲区发送接受消息,当缓冲区不为空recv就不会阻塞
    *TCP粘包
        【1】原因:TCP以字节流方式传输,没有消息边界.
                 多次发送的消息被一次接受,此时就会形成粘包
        【2】影响:如果每次发送的消息是独立的含义,需要接受端
                 独立解析,此时粘包会有影响
        【3】解决方法
                 1.人为的添加消息边界
                 2.控制发送速度
二.UDP套接字编程
    1.服务端流程
        【1】创建数字报套接字    
            sockfd = socket(AF_INET,SOCK_DGRAM)
        【2】绑定地址
            sockfd.bind(addr)
        【3】消息收发
            data,addr = sockfd.recvfrom(buffersize)
            功能:接受UDP消息
            参数:每次最多接受多少字节
            返回值:data 接受的内容
                addr 消息发送方地址
            
            n = sockfd.sendto(data,addr)
            功能: 发送UDP消息
            参数: data 发送的内容 bytes格式
                addr 目标地址
            返回值: 发送的字节数
        【4】关闭套接字
            sockfd.close()

    2.客户端流程
        【1】创建套接字
        【2】收发消息
        【3】关闭套接字

*TCP套接字 和 UDP套接字 编程区别
    1.流式套接字是以字节流方式传输数据，数字报套接字以数据报传输
    2.TCP套接字会有粘包，UDP套接字有消息边界不会粘包
    3.TCP套接字保证消息的完整性，UDP套接字则不能
    4.TCP套接字依赖listen accep建立连接才能收发消息，UDP套接字则不需要
    5.TCP套接字使用send，recv收发消息，UDP套接字使用sendto，recvfrom


二.socket模块方法 和 socket套接字属性
    1.socket模块方法
        【1】gethostname() 获取计算机名
        【2】gethostbyname('www.baidu.com') 获取主机ip地址
        【3】getservbyname('mysql') 获取服务端口号
        【4】getservbyport(3306) 获取端口对应服务
        【5】inet_aton('192.168.1.2') 将IP地址转化成bytes子串
        【6】inet_ntoa(b'\xc0\xa8\x01\x02') 将bytes子串转化成IP地址

    2.套接字属性
        【1】sockfd.type 套接字类型
        【2】sockfd.family 套接字地址类型
        【3】sockfd.getsockname() 获取套接字绑定地址
       *【4】sockfd.fileno() 获取套接字的文件描述符
            文件描述符:系统中每一个IO操作都会分配一个整数作为编号, 
            特点:文件描述符是系统用来区分处理IO的标志,不会重复
       *【5】sockfd.getpeername() 获取连接套接字客户端地址
       *【6】socket.setsockopt(level,option,value)
            功能:设置套接字选项
            参数:level 选项类别(SOL_SOCKET)
                option 具体选项内容
                value 选项值
        【7】sockfd.getsockopt(level,option)
            功能:获取套接字选项值

三.UDP套接字广播
    定义:一端发送多段接受
    地址:每个网络的最大地址为发送广播的地址,向该地址发送,则网段内所有主机

四.TCP套接字之HTTP传输
    1.HTTP协议(超文本传输协议)
        【1】用途:网页获取,数据传输
        【2】特点:　
                *应用层协议,传输层使用TCP传输
                *简单,灵活,很多语言都有HTTP专门接口
                *无状态,协议不记录传输内容
                *HTTP1.1 支持持久连接,丰富了请求类型
        【3】网页请求过程
            1.客户端(浏览器)通过TCP传输,发送HTTP请求给服务端
            2.服务端接受到HTTP请求后进行解析
            3.服务端处理请求内容,组织响应内容
            4.服务端将响应内容以HTTP响应格式发送给浏览器
            5.浏览器收到响应内容，解析展示
        【4】HTTP请求(request)
            *请求行:具体的请求类别和请求内容
                　GET         /      HTTP/1.1
　              请求类别    请求内容    协议版本
            请求类别:每个请求类别表示要做不同的事情
            GET:获取网络资源 
            POST:提交一定的信息,得到反馈
            HEAD:只获取网络资源的响应头
            PUT:更新服务器资源
            DELETE:删除服务器资源
            CONNECT
            TRACE:测试
            OPTIONS:获取服务器性能信息

            *请求头:对请求的进一步解释和描述
             Accept-Encoding:gzip(以键值对形式,每一行一个键值对)
             　
            *空行
             
            *请求体:请求参数或提交内容
        【5】HTTP响应(response)
            1.响应格式:响应行,响应头,空行,响应体
            2.响应行:反馈基本的响应情况
                HTTP/1.1    200     OK
            　　　版本信息　　响应吗   附加信息
                　响应吗:1xx 提示信息,表示请求被接受
                　　　　 2xx 响应成功
                　　　　 3xx 响应需要进一步操作,重定向
                　　　　 4xx 客户端错误
                　　　　 5xx 服务器错误
            3.响应头:对响应内容的描述
                Content-Type:text/html
            4.响应体:响应的主体内容信息
            


作业:
    1.使用TCP完成一个文件的传输,将文件从客户端发送给服务端
    　(要求文件可以是文件,也可以是图片)
    2.记住http 请求格式和请求行每部分含义,了解请求类型
    3.能够自己写出　TCP UDP 的基础代码








s


































































