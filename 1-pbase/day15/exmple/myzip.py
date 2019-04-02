# 此示例示意用生成器函数来创建一个人与zip函数功能一致的函数
#def myzip(*args):
def myzip(iterable1,iterable2):
    it1=iter(iterable1)
    it2=iter(iterable2)
    while True:
        try:
            v1=next(it1)
            v2=next(it2)
        except StopIteration:
            return    

