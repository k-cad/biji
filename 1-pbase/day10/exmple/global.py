v=100
def f1():
    global v#全局声明语句
    v=200

f1()
print(v)
