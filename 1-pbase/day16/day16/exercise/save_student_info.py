# 练习:
#   写一个函数,要求把一个字典组成的列表(学生信息列表)，写入
#       文件si.txt中
#   要求:
#     内容是每个学生的信息写在一行内,每个信息之间用逗号分隔开
#   如:
#     def save_to_file(L):
#         ....

#     L = [dict(name='xiaozhang', age=20, score=100),
#          dict(name='xiaoli', age=18, score=98)
#         ]
#     save_to_file(L)
#     文件si.txt的内容是:
#      xiaozhang,20,100
#      xiaoli,18,98

def save_to_file(L):
    try:
        f = open("si.txt", 'w')
        # 循环写入每个学生的信息
        for d in L:
            # 每次写入一个学生的信息
            f.write(d['name'])  # 姓名
            f.write(',')
            f.write(str(d['age']))  # 年龄
            f.write(',')
            f.write(str(d['score']))  # 成绩
            f.write('\n')  # 换行
        f.close()
        print("保存成功")
    except OSError:
        print("保存失败!")

L = [dict(name='xiaozhang', age=20, score=100),
        dict(name='xiaoli', age=18, score=98)
    ]
save_to_file(L)


