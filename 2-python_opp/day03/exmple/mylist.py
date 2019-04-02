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

    def __add__(self, other):
        return Mylist(self.data + other.data)

    def __mul__(self,value):
        return Mylist(self.data * value)

    def __str__(self):
        ret = ''
        for x in self.data:
            ret += str(x)
            ret += " "
        return ret
        
if __name__ =='__main__':
    L=Mylist([-1,2,-3,5.678])
    L2 = Mylist([5,6,7])
    print(str(L + L2))
    print(str(L * 2))
