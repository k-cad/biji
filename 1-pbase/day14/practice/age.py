def get_age():
    age=int(input('请输入年龄：'))
    if age < 0 or age>140:
        raise ValueError('输入的年龄无效')
    return age

try:
    age=get_age()
    print('用户输入的年龄是：',age)
except ValueError as e:
    print('错误提示：',e)
    print('用户输入的不是1~140的整数，获取年龄失败')