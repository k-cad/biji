# for x in range(4):
#     print(x)
# for x in range(1,10,3):
#     print(x)
# 练习：1,用for 打印1~20的整数，打印在一行内
#      2,打印100以内对11求余等于８的数
#      3,计算1+2+3+4+...+99的和，分别用while 和　for 语句实现
#第一题
#  for x in range(21):
#     print(x,end=" ")
# print()
#第二题
# for x in range(101):
#     if x * (x+1) % 11 == 8:
#         print(x)
#第三题
# for 循环
# s=0
# for x in range(1,100,2):
#     s += x
# print(s)
# while 循环
# s = 0
# x = 1
# while x < 100:
#     s += x
#     x += 2
# print(s) 

i = 6 
for x in range(1,i):
    print('x =',x,'i =',i)
    i -= 1
