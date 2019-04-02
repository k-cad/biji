# my_number.py
# 自定义数字类型
# 数值转换函数重写示例
class MyNumber:
    def __init__(self, value):
        self.data = value #值，字符串
    
    def __int__(self):
        return int(float(self.data))

    def __float__(self):
        return float(self.data)
    
    def __complex__(self):
        return complex(self.data)

if __name__ == "__main__":
    num = MyNumber("123.45")
    print(getattr(num, "data")) # "123.45"
    print(num.data)  # "123.45"

    setattr(num, "data", "456.78")
    print(getattr(num, "data")) #456.78

    print(hasattr(num, "data")) #True
    print(hasattr(num, "aaaa")) #False

    delattr(num, "data") #删除data属性
    print(hasattr(num, "data")) #False
    
    # print(int(num))  #将num对象转换成int
    # print(float(num))
    # print(complex(num))