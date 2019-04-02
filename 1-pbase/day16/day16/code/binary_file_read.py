# binary_file_read.py


# 此示例示意用二进制模式操作文件，实现读取文件myfile.bin数据
# 中的前10个字节

fr = open('./myfile.bin', 'rb')
b = fr.read(10)  # 此方法将返回字节串
print('b=', b)
fr.close()

