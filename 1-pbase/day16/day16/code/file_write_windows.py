

# 此示例示意写文件的基本操作
try:
    # 1. 打开文件
    f = open("mynote.txt", 'w')  # 创建新文件
    # 2. 写文件
    f.write("ABCD\r\n")
    f.write("你好！\r\n")
    # f.write({1:"一"})  # 出错
    f.writelines(["abcd\r\n", '1234\r\n'])
    # 3. 关闭文件
    f.close()
except OSError:
    print("打开文件失败!")



