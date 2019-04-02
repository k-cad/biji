#raise4.py
def get_score():
    '''此函数强制用户输入0~100之间的数，如果输入的是其他的数则直接触发异常来通知调用者'''
    score = int(input('请输入成绩：'))
    if score <0:
        raise ValueError
    if score >100:
        raise ValueError('成绩超出了最大值')
    return score

try:
    score=0
    score=get_score()
except ValueError as err:
    print('用户输入错误，err=',err)

print('学生的成绩是：',score)