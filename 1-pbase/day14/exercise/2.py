def prime_factor(n):
    k=2
    for k in range(2,n+1):
        if n%k==0 and n>k:
            print('%d×'%k,end='')
            n=n//k
        elif n%k==0 and n==k:
            print(n)
            break
    return


a=int(input('请输入一个整数:'))

print('%d='%a,end="")
prime_factor(a)