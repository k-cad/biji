# mydec03.py
# 此示例示意函数装饰器的使用
# 以银行存取款业务为例,来为存取钱业务添加新的功能
# 1,
# 2，
# ------以下为装饰器------
def privileged_check(fn):
    def fx(n,x):
        print('正在检查权限...')
        fn(n,x)
    return fx
def send_message(fn):
    def fy(n,x):
        fn(n,x)
        print('正在发送短信息',n)
#------以下为主程序-------
@privileged_check
def savemoney(name,x):
    print(name,'存钱',x,'元')
@send_message
@privileged_check
def withdraw(name,x):
    print(name,'取钱',x,'元')
#------调用函数------
savemoney('小张',400)

withdraw('小李',500)