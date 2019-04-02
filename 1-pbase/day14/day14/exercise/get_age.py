# 练习:
#   写一个函数 get_age 用来获取一个人的年龄信息
#     此函数规定用户只能输入1~140之间的整数，如果用户输入其它
#     的数则直接触发ValueError类型的错误！
#   如:
#     def get_age():
#         ...  # 此处的逻辑自己实现
#     try:
#        age = get_age()
#        print("用户输入的年龄是:", age)
#     except ValueError:
#         print("用户输入的不是1~140的整数，获取年龄失败")


def get_age():
    age = int(input("请输入年龄(1~140): "))
    if age < 1 or age > 140:
        raise ValueError("年龄不在有效的范围内!")
    return age

try:
    age = get_age()
    print("用户输入的年龄是:", age)
except ValueError:
    print("用户输入的不是1~140的整数，获取年龄失败")

