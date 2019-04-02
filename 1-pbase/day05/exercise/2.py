n=int(input('请输入：'))

# if n==2:
#     print('是素数')
# else:
#     for x in range(2,n):
#         if n%x==0:
#             i = False
#             break
#         else:
#             i=True
#     if i== True:
#         print('是素数')
#     elif i == False:
#         print('不是素数')


if n<2:
    print(n,"不是素数")
else:
    
    for x in range(2,n):
        if n % x == 0:
            print(x,'不是素数')
            break
    else:
        print(x,'是素数')


