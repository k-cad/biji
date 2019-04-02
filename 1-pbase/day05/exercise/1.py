n=int(input('请输入：'))
# i=1
# while i<=n:
#     s='*'*(2*i-1)
    
#     i+=1
#     print(s.center(2*n-1))
# while n<i<=2*n:
#     print('*'.center(2*n-1))
#     i += 1


for x in range(1,n+1):
    c=2*x-1
    s='*'*c
    print(s.center(2*n-1))
# for x in range(n+1)