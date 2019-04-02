#此示例示意写入256个字节到一个文件中
#第一个字节值为0，第二个字节的值为1，...
try:    
    f=open('myfile.bin','wb')
    b=bytes(range(256))
    print(b)
    r=f.write(b)
    print('成功写入',r,'个字节')
    f.close
except OSError:
    print('文件打开失败!')