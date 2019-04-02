
#   3. 计算 1 + 3 + 5 + 7 + .... + 99 的和
#      分别用for循环语句和while循环语句实现
  
# 用for循环实现
# s = 0  # 用来累加和
# for x in range(1, 100, 2):
#     s += x
# print("和是:", s)

# 用while循环实现
s = 0
x = 1
while x < 100:
    s += x  # 累加
    x += 2  # 向后移2

print("用while计算后的的是", s)