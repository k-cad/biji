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

    def __add__(self, other): # L1 + L2  
        return MyList(self.data + other.data)

    def __mul__(self, value): # L1 * 2
        return MyList(self.data * value)
    
    def __eq__(self, other): # 重载==运算符
        len1 = len(self.data)  # 取data属性长度
        len2 = len(other.data) # 取另一个对象data的长度
        if len1 != len2: # 长度不相等，无需比较
            return False

        for i in range(0, len1):
            if self.data[i] != other.data[i]:
                return False #只要出现元素不相等，返回False
        return True 

    def __ne__(self, other): # 重载!=运算符
        return not (self == other) 

    def __gt__(self, other):
        len1 = len(self.data)  # 取data属性长度
        len2 = len(other.data) # 取另一个对象data的长度
        min_len = min(len1, len2) # 获得循环上限

        for i in range(min_len): # 以长度短的作为循环上限
            if self.data[i] == other.data[i]:
                continue
            elif self.data[i] > other.data[i]:
                return True
            elif self.data[i] < other.data[i]:
                return False
        if len1 == len2:  #相等
            return False  
        elif len1 > len2: #前面的元素相等，长度比对方大
            return True
        else:
            return False

    def __neg__(self): #重载符号运算符
        return MyList(-x for x in self.data)

    def __contains__(self, e): # in/not in运算符重载
        print("__contains__()被调用")
        return e in self.data

    def __getitem__(self, i): # 重载[]取值操作
        return self.data[i] 
    
    def __setitem__(self, i, value):#重载[]赋值操作
        self.data[i] = value

    def __delitem__(self, i): #重载[]删除操作
        del self.data[i]

if __name__ == "__main__":
    L = MyList([-1, 2, -3, 4, -5])
    print(L[0])  # 索引取值
    L[2] = 333   # 通过索引设置值
    print(L)
    del L[3]     # 删除
    print(L)

    # print(2 in L)   # True
    # print(4 not in L) # False

    #print(-L)  # 对对象执行负号运算

    # L1 = MyList([1,3,5])
    # L2 = MyList([1,3,5,7])
    # print(L1 > L2)
    # L = MyList([-1, 2, -3, 5.6789])
    # L3 = MyList([3,4,5])
    # print(L + L3)
    # print(L * 2)
    # print(2 * L)

    # print(reversed(L))  # 对象元素逆序并打印
    # print(len(L))   # 打印返回的长度
    # print(round(L)) # 打印新产生的对象
    #                 # 每个元素都是原对象元素的近似值
    # L2 = abs(L)  # 重写了__abs__()函数，支持abs表达式
    # print(L2)  # 重写了__str__()函数，所以支持print()