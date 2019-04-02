
def input_student(L):
    while True:
        n=input('请输入姓名:')
        if not n:
            break
        a=input('请输入年龄:')
        if not a:
            break
        s=input('请输入成绩:')
        if not s:
            break
        d={'name':n,'age':a,'score':s}
        L.append(d)
    return L


def get_chinese_char_count(n):
    c=0
    for  x in n:
        # if int('0x4e00',base=16)<=ord(x)<=int('0x9fa5',base=16):
        if 0x4e00<=ord(x)<=0x9fa5:
            c += 1
    return c

def output_student(L):
    print("+---------------+-----------+----------+")
    print("|     姓名      |    年龄   |   成绩   |")
    print("+---------------+-----------+----------+")
    for d in L:
        n = d['name']
        a = d['age']
        s = d['score']
        a = str(a)  
        s = str(s)
        print("|" + n.center(15-get_chinese_char_count(n)) + '|'
                  + a.center(11) + '|'
                  + s.center(10) + '|')
    print("+---------------+-----------+----------+")

def change_student(L):
    n =input('请输入需要修改成绩的学生姓名')
    for x in L:
        if x['name']==n:
            s=int(input('请输入更正后的成绩'))
            x['score']=s
        else:
            print('未找到该生')

def remove_student(L):
    n=input('请输入需要修改信息的学生姓名')
    i=0
    for x in L:
        
        if x['name']==n:
            L.remove(x)
        else:
            print('未找到该生')
def reverse_age(d):
    k=d['age']
    return k
def reverse_score(d):
    k=d['score']
    return k
    
def show_menu():
    print("++++++++++++++++++++++++")
    print('|1)添加学生信息        |')
    print('|2)显示学生信息        |')
    print('|3)删除学生信息        |')
    print('|4)修改学生信息        |')
    print('|5)按照成绩从高到低排序|')
    print('|6)按照成绩从低到高排序|')
    print('|7)按照年龄从大到小排序|')
    print('|8)按照成绩从小到大排序|')
    print('|q)退出                |')
    print("++++++++++++++++++++++++")
def main():
    L=[]
    while True:
        show_menu()
        s=input('请选择：')
        if s=='1':
            input_student(L)
        elif s=='2':
            output_student(L)
        elif s== '3':
            remove_student(L)
        elif s== '4':
            change_student(L)
        elif s=='5':
            L2=sorted(L,key=reverse_score,reverse=True)
            output_student(L2)
        elif s=='6':
            L2=sorted(L,key=reverse_score)
            output_student(L2)
        elif s=='7':
            L2=sorted(L,key=reverse_age,reverse=True)
            output_student(L2)
        elif s=='8':
            L2=sorted(L,key=reverse_age)
            output_student(L2)
        elif s=='q':
            break

main()


