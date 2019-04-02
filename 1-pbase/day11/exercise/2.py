#第一问
def print_list(L,line=False):
    for x in L:
        if type(x) is int:
            print(x,end=' ')
        else:
            print_list(x)
L = [[3,5,8],10,[[13,14],15,18],20]
print_list(L,True)
# #第二问
# def sum_list(L):
#     s=0 
#     for x in L:
#         if type(x) is int:
#             s += x
#         else:
#             s += sum_list(x)
#     return s      
# L = [[3,5,8],10,[[13,14],15,18],20]   
# print(sum_list(L))
