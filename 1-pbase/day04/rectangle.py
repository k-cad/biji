# 输入一个整数n,打印一个高度和宽度都为n个字符的长方形
n = int(input('请输入宽度：'))
# 第一行
print('#'*n)
# 中间部分
i = 1
while i <= n-2:
    print('#'+' '*(n-2)+'#')
    i += 1
if n >= 2:
    print('#'*n)



