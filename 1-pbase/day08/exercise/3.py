
def input_student():
    L = []
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
        n=d['name']
        a = d['age']
        s = d['score']
        a = str(a)  
        s  = str(s)
        print("|" + n.center(15-get_chinese_char_count(n)) + '|'
                  + a.center(11) + '|'
                  + s.center(10) + '|')
    print("+---------------+-----------+----------+")

infos = input_student()
print(infos)
output_student(infos)
