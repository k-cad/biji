
class A:
    def __init__(self, name):
        self.name = name

    def __str__(self):  # 重写__str__函数
        return "name = %s" % self.name

class B(A):
    def __init__(self, name, id):
        super().__init__(name) # 调用父类构造方法
        self.id = id  # id属性被创建

    def __repr__(self):  # 重写__repr__方法
        # 返回例如"B('Jerry','0001')"
        return "B('%s','%s')" % (self.name, self.id)

    def __str__(self):  # 重写__str__函数
        return "name=%s,id=%s"%(self.name,self.id)

b = B("Jerry", "0001")  # ==》
print(b) 

# str_obj = repr(b)
# print(str_obj)
# new_obj = eval(str_obj)  # 通过调用eval函数还原对象
# print(new_obj)

# print(b)  # B类中重写__str__方法，所以可以直接打印
# str_obj = str(b)  # 将b对象转换成字符串
# print(str_obj)

#super(B, b).print() # 根据对象b找到父类，并调用父类的print
# print(issubclass(B, (A,object)))    # True
# print(issubclass(B,object)) # True
# print(issubclass(A, B))  # False