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
except (ValueError,ZeroDivisionError) as err:
    print('分苹果失败，苹果被收回')
    print('err=',err)
    print('程序退出')
else:#此子句里的语句只有在try语句内没有异常时才执行
    print('此try语句中没有发生错误，else语句执行')
finally:
    print('这是try语句中的 finally语句，一定会被执行！')

