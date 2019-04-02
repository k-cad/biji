class A:
    def __init__(self,name):
        self.name=name
    def print(self):
        print('name = %s' % self.name)
    # def __str__(self):
    #     return 'name = %s' % self.name
class B(A):
    def __init__(self,name,id):
        super().__init__(name)#调用父类构造方法
        self.id=id
    def __repr__(self):
        return "B('%s','%s')" % (self.name,self.id)
    # def __str__(self):
        # return 'name = %s,id = %s' % (self.name,self.id)
    
b = B('alan','001')
str_obj=repr(b)
print(str_obj)
new_obj=eval(str_obj)#通过调用eval函数还原对象
print(new_obj)



# print(b)

# str_obj=str(b)
# print(str_obj)

# super(B,b).print()
# print(b.id)
# print(b.name)

# print(issubclass(B,A))
# print(issubclass(B,object))
# print(issubclass(A,B))
