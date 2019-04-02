# 此示例示意打开一个文件，同时对文件进行读写操作
try:
    #1打开文件
    f=open('myfile.txt')
    print('文件打开成功')
    #2读取文件
    s=f.read()
    print('读取字符的个数是：',len(s))
    print('文件的内容是：',s)
    #3关闭文件
    f.close()
    print('文件关闭成功')
except OSError:
    print('打开文件失败!!!')