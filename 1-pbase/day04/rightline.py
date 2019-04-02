#练习：
#   写一个程序输入三行文字，让这三行字符依次以
#    20个字符的宽度右对起输出
a=input('请输入第一行:')
b=input('请输入第二行:')
c=input('请输入第三行:')
# 第一问
# print('%20s'%a)
# print('%20s'%b)
# print('%20s'%c)
#第二问
#求最大长度
m=max(len(a),len(b),len(c))
print(m)
#法一
#print()
#法二

fmt='%'+str(m)+'s'
print(fmt % a) 
print(fmt % b)
print(fmt % c)