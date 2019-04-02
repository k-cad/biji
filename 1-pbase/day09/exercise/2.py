#完全数：
# 1+2+3=6(6为完全数)
# 1,2,3都为6的因数

# L=[]
# for x in range(2,10000):
#     L1=[1]
#     for y in range(2,x):
#         if x%y==0:
            
#             L1.append(y)
#     if x==sum(L1):
#         L.append(x)

# print(L)
def is_prefect_number(x):
    L=[]
    for i in range(1,x):
        
def main():
    i=2
    while True:
        if is_prefect_number(i):
            print(i)
        i += 1
main()
