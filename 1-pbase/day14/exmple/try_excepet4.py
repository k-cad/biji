#try-except语句的语法和用法


def div_apple(n):
    print(n,'个苹果你想分给几个人？')
    s=input('请输入人数:')
    cnt=int(s)
    reslut=n/cnt
    print('每人分了',reslut,'个苹果')

try:
    div_apple(10)
    print('分苹果成功！')
except ValueError:
    print('分苹果失败，苹果被收回')
    print('程序退出')
except:#用来捕获除ValueError类型之外的全部类型的异常错误
    print('其他类型错误！')


