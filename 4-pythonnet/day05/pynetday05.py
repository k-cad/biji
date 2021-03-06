1.fork的运行特征 
    * 子进程会复制父进程的全部内存空间，从fork的下一句开始执行
    * 父子进程各自独立运行，执行顺序不确定
    * 通常情况下fork与if结构是固定搭配，利用父子进程中fork的返回值差异使其各自执行不同的内容
    * 父进程在fork之前开辟的内存空间子进程同样会拥有，父子进程各自对各自空间的操作互不影响
    * 父子进程有各自的特征，比如PID PCB 命令集。
进程相关的函数
1.os.getpid()
    功能:获取当前进程的PID号
    返回值:PID
2.os.getppid()
    功能:获取父进程的PID号
    返回值:PID
3.os._exit(status)
    功能:结束一个人进程
    参数:进程的退出状态(整数)
4.sys.exit([status])
    功能:结束一个进程
    参数:整数表示进程退出状态　默认为0
        字符串则表示进程退出时打印内容

三.孤儿和僵尸
1.孤儿进程:父进程先于子进程退出,此时子进程成为孤儿进程
    特点:孤儿进程会被系统进程收养,此时系统进程就会成为
        孤儿进程的父进程
2.僵尸进程:子进程先于父进程退出,父进程又没有处理子进程
        的退出状态,此时子进程就会成为僵尸进程
    特点:僵尸进程虽然已经结束,但是会存留部分信息在PCB中,
        大量的僵尸进程会浪费系统内存资源
3.如何避免僵尸进程
    【1】使用wait函数处理子进程退出状态
        pid,status = os.wait()
        功能:父进程中阻塞等待处理子进程的退出
        返回值:pid 退出的子进程的pid号
        　　　　status 子进程的退出状态
        pid,status = os.waitpid(pid,option)
        功能:父进程中阻塞等待处理子进程的退出
        参数:pid -1 表示等待任意子进程退出
                >0 表示等待指定子进程退出
            option     0     表示阻塞等待
                    WONHANG  表示非阻塞
        返回值:pid 退出的子进程的pid号
            　status 子进程的退出状态
    【2】创建二级进程处理僵尸
        1.父进程创建子进程,等待回收
        2.子进程创建二级子进程后立即退出
        3.二级子进程成为孤儿,和原父进程一同执行事件
    【3】通过信号处理子进程退出
        原理:子进程退出时会由操作系统给父进程发送信号
            如果父进程忽略这个信号则子进程的退出由操作
            系统自动处理   
        方法:使用signal模块忽略信号
            impo

四.群聊聊天室
    1.功能:群聊功能
        【1】有人进入聊天室需要输入姓名,姓名不能重复
        【2】有人进入聊天室,其他人会收到通知
                xxx进入聊天室
        【3】一个人发消息,其他人会收到消息
                xxx:xxx
        【4】有人退出聊天室,其他人也会收到通知
                xxx退出聊天室
        【5】扩展功能:服务端消息公告,服务端发送消息所有人都能收到
                管理员消息:xxxxxx
    2.确定技术模型
        【1】服务端处理请求,发送管理员消息
            客户端执行各种功能
        【2】UDP套接字
        【3】消息发送模块:转发
            客户端---->服务端---->其他客户端
        【4】储存用户信息｛name:addr｝
        【5】处理收发关系:多进程分别处理收发
    3.注意事项
        【1】设计封装方案
        【2】写一个模块测试一个模块
        【3】注释的添加
    4.具体实现流程
        【1】搭建网络模型
        【2】进入聊天室
                1.客户端:*输入姓名
                        *发给服务器
                        *接收服务器反馈
                        *不允许则重新输入,允许则进入聊天室
                        *创建新的进程用于消息收发
                2.服务端:*接受信息
                        *判断是否允许进入
                        *将结果反馈给客户端
                        *如果不允许则结束,允许将用户插入数据结构
                        *给其他人发送通知
        【3】聊天
                1.客户端:*循环发送消息
                        *循环接收消息
                2.服务端:*接收消息，判断消息类型
                        *
        【4】退出聊天室
        【5】管理员消息

作业:1.将现有聊天室代码整体
    2.尝试自己完成剩余功能
    3.fork进程整理,能够掌握运行原理
    4.类的设计

    

