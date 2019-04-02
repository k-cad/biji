#此示例示意用二进制模式操作文件，实现读取文件myfile.bin数据的前十位

fr = open ('myfile.bin','rb')
b=fr.read(10)
print('b=',b)
fr.close()