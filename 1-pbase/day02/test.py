s=int(input("输入里程:"))
if 0<=s<3:
    print('价格为',13,'元')
elif 3<=s<15:
    c=13+2.3*(s-3)
    print('价格为：',c,'元')
else:
    c=13+2.3*(s-3)+3.45*(s-15)
    m=round(c,2)
    print('价格为',m,'元')