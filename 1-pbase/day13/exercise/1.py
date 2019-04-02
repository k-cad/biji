def password():
    count =0
    L=[str(x) for x in range(10)]
    L+=[chr(x) for x in range(ord('a'),ord('z'))]
    L+=[chr(x) for x in range(ord('A'),ord('Z'))]
    # print(L)
    password=''
    for _ in range(6):
        import random
        password+=random.choice(L)
    print('密码是：',password)    
       

password()