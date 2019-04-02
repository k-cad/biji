# pass.py

# 让程序输入一个学生的成绩(0~100之间),如果不在这个范
# 围内则报错

score = int(input("请输入学生成绩(0~100): "))

if 0 <= score <= 100:
    # print("成绩合法")
    pass
else:
    print("成绩不合法,输入有错!")


