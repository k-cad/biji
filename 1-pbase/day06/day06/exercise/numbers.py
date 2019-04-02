#   2. 写一个程序,让用户输入两个或以上的正整数,当输入小于零的数
#      时结束输入(不允许输入重复的数)
#      1) 打印这些数的和
#      2) 打印这些数的最大数
#      3) 打印这些数的最二大的数
#      4) 删除最小的一个数,并打印原来的列表

numbers = []  # 创建一个容器,用变量numbers绑定
while True:
    x = int(input("请输入正整数: "))
    if x < 0:
        if len(numbers) < 2:
            print('您输入的数字太少')
            continue
        break
    if x not in numbers:
        numbers += [x]

print("这些数的和是:", sum(numbers))
L = sorted(numbers)
print("最大数是:", L[-1])
print("第二大数是:", L[-2])
min_number = L[0]
for i in range(len(numbers)):
    if numbers[i] == min_number:
        del numbers[i]
        break

print("删除最小数后的列表是: ", numbers)
