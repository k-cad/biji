def get_score():
    s=input('请输入成绩：')
    
    try:
        n=int(s)
    except ValueError:
        return 0
    if n<0 or n>100:
        return 0
    return n
score=get_score()
print('学生成绩是',score)