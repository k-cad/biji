count=0
def fx(name):
    print('你好',name)
    global count
    count += 1


fx('小航')
fx('小李')
print('fx函数共被调用',count,'次')