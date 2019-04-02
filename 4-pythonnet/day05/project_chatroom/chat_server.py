# coding=utf-8

'''
Chat room
env: python3.5
exc: socket and fork
name: tech
email:...
'''

from socket import *
import os,sys

#储存客户{name:addr}
user = {}

def do_login(s,name,addr):
    if (name in user) or ('Manager' in name) :
        s.sendto("Name Occupied".encode(),addr)
        return
    s.sendto(b"OK",addr)
    #通知其他人
    msg = "\nWelcome %s into chatroom" % name
    for i in user:
        s.sendto(msg.encode(),user[i])
    #添加用户
    user[name] = addr

def do_chat(s,name,text):
    msg = "\n%s : %s"%(name,text)
    # msg = '\r' + msg +'\nmessage:'
    for i in user:
        if i != name:
            s.sendto(msg.encode(),user[i])

def do_quit(s,name):
    msg = "\n%s Out" % name
    for i in user:
        if i != name:
            s.sendto(msg.encode(),user[i])
        elif i == name:
            s.sendto(b'EXIT',user[i])
    #删除用户
    del user[name]
#处理客户端请求
def do_request(s):
    while True:
        #接受所有客户端请求
        data,addr = s.recvfrom(1024)
        # print(data.decode()) # 请求内容
        msgList = data.decode().split(" ")
        #区分请求类型
        if msgList[0] == "L":
            do_login(s,msgList[1],addr)
        elif msgList[0] == 'C':
            text = " ".join(msgList[2:])
            do_chat(s,msgList[1],text)
        elif msgList[0] == 'Q':
            do_quit(s,msgList[1])


#创建网络连接
def main():
    ADDR = ('0.0.0.0',8888)
    #创建UDP套接字
    s = socket(AF_INET,SOCK_DGRAM)
    s.bind(ADDR)
    
    #创建单独进程用于发送管理员消息
    pid = os.fork()
    if pid < 0:
        print("Create Process failed")
        return
    elif pid == 0:
        while True:
            msg = input("Message From Manager:")
            msg = "C Manager " + msg
            s.sendto(msg.encode(),ADDR)
    else:
        #处理各种客户端请求
        
        do_request(s)

main()
