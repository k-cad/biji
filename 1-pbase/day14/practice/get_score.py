def get_score():
    n=int(input('请输入成绩：'))
    if n<0 or n>100:
        return 0
    return n
try:
    score=get_score()
except ValueError:
    score=0
print('学生成绩是',score)