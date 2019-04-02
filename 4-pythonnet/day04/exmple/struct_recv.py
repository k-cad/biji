from socket import *
import struct

s = socket(AF_INET,SOCK_DGRAM)
s.bind(('127.0.0.1',8888))

st = struct.Struct('i16sf')

while True:
    data,addr = s.recvfrom(1024)
    data = st.unpack(data)
    print