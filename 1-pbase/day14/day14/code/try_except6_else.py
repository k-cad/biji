

# 此示例示意try-except语句的语法和用法

def div_apple(n):
    print(n, '个苹果你想分给几个人?')
    s = input('请输入人数: ')
    cnt = int(s)      # <-- 可能触发ValueError错误
    result = n / cnt  # <--可能触发ZeroDivisionError错误
    print("每个人分了", result, '个苹果')


try:
    div_apple(10)
    print("分苹果成功!")
except ValueError:
    print("分苹果失败!苹果被收回!")
else:  # 此子句里的语句只有在此try内没有发生异常时才执行
    print("此try语句中没有发生错误，此else子句会执行!")



print("程序正常退出")


