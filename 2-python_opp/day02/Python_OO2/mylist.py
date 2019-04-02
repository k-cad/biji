# mylist.py
# 自定义列表
class MyList:
    def __init__(self, iterable=[]):
        self.data = [x for x in iterable]
    
    # 重写__abs__()函数
    def __abs__(self):
        #对每个元素求绝对值，用产生的结果实例化一个MyList对象
        return MyList(abs(x) for x in self.data)
    
    def __str__(self):  # 重写__str__()函数
        ret = ""
        for x in self.data:
            ret += str(x)  # 将元素由数字转换成字符串
            ret += " "
        return ret   # 返回结果串

    def __len__(self):  # 重写__len__函数，返回元素个数
        return len(self.data)

    # 对每个元素求近似值，并实例化对象返回
    def __round__(self): 
        return MyList(round(x,2) for x in self.data)

    # 重写__reversed__，倒序
    def __reversed__(self):
        tmp = []
        x = len(self.data) - 1  # 最后元素下标
        while x >= 0:
            tmp.append(self.data[x])
            x -= 1   # 计数器减1
        return MyList(tmp)  # tmp是经过倒序的可迭代对象

if __name__ == "__main__":
    L = MyList([-1, 2, -3, 5.6789])
    print(reversed(L))  # 对象元素逆序并打印
    print(len(L))   # 打印返回的长度
    print(round(L)) # 打印新产生的对象
                    # 每个元素都是原对象元素的近似值
    L2 = abs(L)  # 重写了__abs__()函数，支持abs表达式
    print(L2)  # 重写了__str__()函数，所以支持print()