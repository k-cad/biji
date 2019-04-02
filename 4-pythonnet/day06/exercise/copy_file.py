from multiprocessing import Process 
import os
from time import sleep

filename  = "./Jenyfa Duncan - Australia.ogg"
# 获取文件大小
size = os.path.getsize(filename)

# 复制上半部分
def top():
    n = size // 2
    fr = open(filename,'rb')
    fw = open('top.ogg','wb')

    while True:


def bot():
    fr = open(filename,'rb')
    fw = open('bot.ogg','wb')
    fr.seek(size//2,0)

    while True:
        if n < 1024:
            fw.write(fr)


t = Process(target = top)
b = Process(target = bot)