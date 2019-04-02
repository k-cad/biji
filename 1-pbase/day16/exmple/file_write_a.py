#此示例示意写文件的基本操作



try:
    #1，打开文件
    f=open('mynote.txt','a')
    #2,写文件
    f.write('ABCD')
    f.write('你好！')
    f.writelines(['1234','ABCD'])
    #3，关闭文件
    f.close()
except OSError:
    print('打开文件失败')