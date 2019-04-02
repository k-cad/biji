#   3. 写程序求:
#     1/1 + 1/3 + 1/5 + 1/7 + ...... + 1/99 的和

s = 0  # 用于累加
fenmu = 1
while fenmu <= 99:
    s += 1 / fenmu
    fenmu += 2

print(s)
