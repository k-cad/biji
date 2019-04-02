#练习：写一个函数mysum可以传入任意个数字参数，返回所有实参的和
def mysum(*args):
    return sum(args)
print(mysum(1,2,3,4))