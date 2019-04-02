# binary_file_write.py

# 此示例示意写入256个字节到一个文件中
# 第一个字节为值为0, 第二个字节的值为１，....以此类推
try:
    f = open('myfile.bin', 'wb')  # 'wb'为二进制写操作
    b = bytes(range(256))  # 创建一个256个字节的字节串
    print(b)
    r = f.write(b)  # 写入256个字节到文件中
    print("成功写入", r, '个字节')  # 注f.write()返回值为写
                                # 入的字节数
    f.close()
except OSError:
    print("文件打开失败!")