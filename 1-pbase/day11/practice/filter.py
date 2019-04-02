L=list(filter(lambda x: x%2==0,range(20)))
print(L)

def is_prime(x):
    if x<2:
        return False
    for i in range(2,x):
        if x%i==0:
            return False

    return True

L1=list(filter(is_prime,range(100)))
print(L1)
L2=[x for x in filter(is_prime,range(100))]
print(L2)
L3=[x for x in range(100) if is_prime(x)]
print(L3)
