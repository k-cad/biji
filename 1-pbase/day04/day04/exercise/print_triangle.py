# 练习:
#   用while语句实现打印三角形,输入一个整数,表示三角形的宽度
#   和高度,打印出相应的三角形
#     如:
#       请输入三角形的宽度: 4
#     1) 打印如下三角形
#       *
#       **
#       ***
#       ****
#     2) 打印如下三角形:
#          *
#         **
#        ***
#       ****
#     3)  打印如下三角形:
#       ****
#        ***
#         **
#          *
#     4)  打印如下三角形:
#       ****
#       ***
#       **
#       *


w = int(input("请输入三角形的宽度: "))
stars = 1  # start 代表星号的个数,也是行数
while stars <= w:
    print('*' * stars)
    stars += 1

print('-------------------')
stars = 1  # 代表星号和行号
while stars <= w:
    # 计算出左侧空格的个数
    blank = w - stars
    print(' ' * blank + '*' * stars)
    stars += 1

print('+++++++++++++++++++++++++++')
stars = w  # stars 代表星号个数
while stars > 0:
    # 此处按星号个数,和w的宽度打印一行
    blank = w - stars  # 计算空格个数
    print(' ' * blank + '*' * stars)
    stars -= 1  # 每一行过后,让星号少一个

print('==========================')
stars = w  # stars 代表星号个数
while stars > 0:
    print('*' * stars)
    stars -= 1
# 4)  打印如下三角形:
#     ****
#     ***
#     **
#     *








