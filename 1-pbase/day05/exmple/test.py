s=input('输入一个字符串')

# blanks_count=0

# for ch in s:
#     if ch == ' '
#     blanks_count += 1
# print('空格的个数为'，blanks_count)
count= 0
for ch in s:
    if 65 <= ord(ch)<91 or 97<=ord(ch)<=123:
    # if 'A' <= ch <= 'Z' or 'a' <= ch <= 'z':
        count += 1
print ('字母个数：',count)