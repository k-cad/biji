#   4. 实现带界面的学生信息管理程序
#     界面如下:
#     +----------------------+
#     | 1) 添加学生信息        |
#     | 2) 查看学生信息        |
#     | 3) 删除学生信息        |
#     | 4) 修改学生成绩        |
#     | q) 退出               |
#     +----------------------+
#     请选择:1
#     请输入学生姓名: xiaozhang
#     请输入学生年龄: 20

#     要求每个功能写一个函数与之相对应(复用之前的学生信息
#     管理程序)

def input_student():
    # 此函数用于返回所有用户输入的学生信息的列表
    infos = []  # 创建一个列表容器准备存放每个学生信息的字典
    while True:
        n = input("请输入姓名: ")
        if not n:  # 如果姓名为空,则结束输入
            break
        a = int(input("请输入年龄: "))
        s = int(input("请输入成绩: "))
        # 新创建一个字典 {}  dict()
        d = {'name':n, 'age':a, 'score':s}  # d = dict(name=n, age=a, score=s)
        infos.append(d)
    return infos

def output_student(L):
    # 此函数以表格形式打印学生信息
    print("+---------------+-----------+----------+")
    print("|     姓名      |    年龄   |   成绩   |")
    print("+---------------+-----------+----------+")
    for d in L:  # d绑定字典
        n = d['name']
        a = d['age']
        s = d['score']
        a = str(a)  # 将整数转为字符串
        s = str(s)
        print("|" + n.center(15) + '|'
                + a.center(11) + '|'
                + s.center(10) + '|')
    print("+---------------+-----------+----------+")

def remove_student(L):
    # 获取要删除人的姓名
    n = input("请输入要删除人的姓名: ")
    i = 0  # 开始索引
    while i < len(L):
        if L[i]['name'] == n:
            del L[i]  # 删除索引
            print("删除成功!")
            return # 删除完毕
        i += i

def modify_student_score(L):
    n = input("请输入要修改成绩的人的姓名: ")
    s = int(input("请输入新成绩: "))
    print(".....")

def show_menu():
    print("+------------------------+")
    print("| 1) 添加学生信息        |")
    print("| 2) 查看学生信息        |")
    print("| 3) 删除学生信息        |")
    print("| 4) 修改学生成绩        |")
    print("| q) 退出                |")
    print("+------------------------+")

def main():
    '''主函数,此函数最先运行'''
    infos = []  # 此列表用来保存所有学生的信息的字典
    # 进入主事件循环
    while True:
        show_menu()
        s = input("请选择: ")
        if s == 'q':
            return  # 退出main函数
        elif s == '1':
            infos += input_student()
            # infos.extend(input_student())
        elif s == '2':
            output_student(infos)
        elif s == '3':
            remove_student(infos)
        elif s == '4':
            modify_student_score(infos)

main()



