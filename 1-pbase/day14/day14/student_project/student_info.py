# file: student.py
    
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

def delete_student(L):
    name = input("请输入要删除学生的姓名: ")
    i = 0  # i 代表列表的索引
    while i < len(L):
        d = L[i]  # d绑定字典
        if d['name'] == name:
            del L[i]
            print("删除", name, "成功!")
            break
    else:
        print("删除失败!")

def modify_student_score(L):
    pass


def output_by_score_desc(L):
    def get_score(d):
        return d['score']
    L2 = sorted(L, key=get_score, reverse=True)
    output_student(L2)

def output_by_score_asc(L):
    L2 = sorted(L, key=lambda d:d['score'])
    output_student(L2)

def output_by_age_desc(L):
    L2 = sorted(L, key=lambda d:d['age'], reverse=True)
    output_student(L2)

def output_by_age_asc(L):
    L2 = sorted(L, key=lambda d:d['age'])
    output_student(L2)




