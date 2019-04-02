#此示例示意文件缓冲的作用及清倒(清除)

fw=open('myflush.txt','w')
fw.write('hello')
fw.flush()
import time
while True:
    time.sleep(0.1)
    fw.write('A'*100)
    pass

fw.close()
