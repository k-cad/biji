#   2. 中国古代的秤是16两一斤，请问古代的216两是古代的几斤几两?
#      写程序打印出来

all_liang = 216

jin = all_liang // 16  # 得到古代的斤
liang = all_liang % 16  # 得到古代的两
print(all_liang, "是古代的", jin, '斤', liang, '两')

