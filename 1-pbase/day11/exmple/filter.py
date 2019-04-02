# def is_odd(x):
#     return x%2==1

# for x in filter(is_odd,range(20)):
#     print(x)

# for x in filter(lambda x:x%2==1,range(10)):
#     print(x)

L=list(filter(lambda x: x%2==1,range(10)))
print(L)