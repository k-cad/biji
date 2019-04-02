#此示例示意用def语句没有参数的函数
# def say_hello():
#     print('hello world')
#     print('hello China')
#     print('hello python')
# say_hello()
# 此示例示意用def语句来定义带有参数的函数
# 此函数名为mymax,有两个形式参数a,b用于接受实参的传递
# 此函数计算两个参数的最大值并打印

# def my_max(a,b):
#     print('a=',a)
#     print('b=',b)
#     if a>b:
#         print(a,'大于',b)
#     else:
#         print(a,"小于等于",b)

# my_max(100,200)


# 练习：写一个函数myadd,此函数中的参数列表中有两个参数x,y
# 此函数的功能是打印x+y的和
# 如：
# def myadd(x,y):
#     print(x+y)
# myadd(100,200)
# myadd('ABC','123')




#练习 写一个函数print_event,传入一个参数n代表终止的整数，打印0~n之间所有的偶数
#如：
def print_event(n):  
    for x in range(0,n+1,2):  
        print(x)
print_event(10)


        
