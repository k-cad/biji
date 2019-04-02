#输入三行字让这三行字在方框中居中显示
a =input('请输入第一行英文：')
b =input('请输入第二行英文：')
c =input('请输入第三行英文：')
max_len = max(len(a),len(b),len(c))
line1='+-'+'-'*max_len+'-+'
print(line1)
print('| '+a.center(max_len)+' |')
print('| '+b.center(max_len)+' |')
print('| '+c.center(max_len)+' |')
print(line1)