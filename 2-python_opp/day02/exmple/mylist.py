#mylist.py
#自定义列表
class Mylist:
    def __init__(self,iterable = []):
        self.data = [x for x in iterable]
    # 重写__abs__()函数
    def __abs__(self):
        return Mylist(abs(x) for x in self.data)
    
    def __len__(self):
        return len(self.data)
    
    def __round__(self):
        return Mylist(round(x,2) for x in self.data)
    
    def __reversed__():
        tmp = []
        x = len(self.data)
        while x >= 0:
            tmp.append(self.data[x])
            x -= 1
        return Mylist(tmp)

    def __str__(self):
        ret = ''
        for x in self.data:
            ret += str(x)
            ret += " "
        return ret
        
if __name__ =='__main__':
    L=Mylist([-1,2,-3,5.678])
    # L2=abs(L) #重写了__abs__()函数，支持abs表达式
    # print(L2) 
    print(abs(L))
    print(len(L))
    print(round(L))
    #打印自定义列表中所有元素的绝对值
    # for x in L.data:
    #     print(abs(x))
    #取所有元素近似值打印
    # for x in L.data:
    #     print(round(x,2))
