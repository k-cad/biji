from socket import *
from time import sleep

#目标地址
dest = ('176.5.17.255',9999)

s = socket(AF_INET,SOCK_DGRAM)

s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)

data = '''撩一下，就走'''
while True:
    sleep(2)
    s.sendto(data.encode(),dest)

s.close()