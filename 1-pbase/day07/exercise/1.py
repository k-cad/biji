# 1,思考下面的程序的执行结果是什么？
L = list(range(10))
for x in L:
    L.remove(x)
print('L=',L)#请问是空列表吗