#此示例示意文件缓冲的作用及清倒(清除)

fw=open('myflush.txt','w')
fw.write('hello')

while True:
    pass

fw.close()
