
#   3. 改写之前的学生信息管理程序:
#     用两个函数来封装功能的代码块
#        函数1:  input_student()   # 返回学生信息字典的列表
#        函数2:  output_student(L)  # 打印学生信息的表格
    
def input_student():
    L = []  # 创建一个列表,准备存放学生数据的字典
    while True:
        n = input("请输入姓名: ")
        if not n:  # 如果用户输入空字符串就结束输入
            break
        a = int(input("请输入年龄: "))
        s = int(input("请输入成绩: "))
        d = {}  # 一定要每次都创建一个新的字典
        d['name'] = n
        d['age'] = a
        d['score'] = s
        L.append(d)   # 把d加入列表中L
    return L

def output_student(L):
    print("+---------------+----------+----------+")
    print("|     姓名      |   年龄   |   成绩   |")
    print("+---------------+----------+----------+")
    for d in L:
        name = d['name']
        age = str(d['age'])  # 转为字符串
        score = str(d['score'])  # 转为字符串
        print("|%s|%s|%s|" % (name.center(15), 
                            age.center(10),
                            score.center(10)))
    print("+---------------+----------+----------+")


infos = input_student()
print(infos)  # 打印列表[{...}, {...}]
output_student(infos)   # 根据实参infos打印表格
   