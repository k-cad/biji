# 已知有五位朋友
# 第五个人说他比第四个人大两岁
# 第四个人说他比第三个人大两岁
# 第三个人说他比第二个人大两岁
# 第二个人说他比第一个人大两岁
# 第一个人说他10岁
def age(n):
    if n==1:
        return 10
    else:
        return 2 + age(n-1)
print(age(5))
print(age(3))