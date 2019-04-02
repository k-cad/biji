# flush.py


# 此示例示意文件缓冲的作用及清倒(清除)方法

fw = open("myflush.txt", 'w')

fw.write("hello")  # 此处执行的write操作没有真正写在磁盘上

import time
while True:  # 进入死循环
    time.sleep(0.1)
    print(time.time())
    fw.write('A'*1000+'\n')

fw.close()
