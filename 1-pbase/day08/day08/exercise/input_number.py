#  3 写一个函数 input_number
#     def input_number():
#         ....  # 此处自己实现,此函数返回列表

#     此函数用来获取用户循环输往返整数,当用户输入负数时结束输入
#     将用户输入的数字以列表的形式返回,再用内建函数max,min,
#     sum 求出用户输入的最大值,最小值及和

#     L = input_number()
#     print("用户输入的最大数是:", max(L))
#     print("用户输入的最小数是:", min(L))
#     print("用户输入的全部数的和是:", sum(L))




def input_number():
    # 1. 创建空列表
    myL = []
    # 2. 循环读取用户输入的正整数,存入在述列表
    while True:
        x = int(input("请输入正整数: "))
        if x < 0:
            break
        myL.append(x)
    # 3. 返回上述列表的引用关系 
    return myL

L = input_number()
print("用户输入的最大数是:", max(L))
print("用户输入的最小数是:", min(L))
print("用户输入的全部数的和是:", sum(L))
