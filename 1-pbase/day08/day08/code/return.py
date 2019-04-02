# return.py

# 此示例示意return语句在函数中的应用

def say_hello2():
    print("hello aaa")
    print("hello bbb")
    return  # 等同于 return None
    # return 1 + 2
    # return [1, 2, 3, 4]
    print("hello ccc")

v = say_hello2()
print("v=", v)

v2 = say_hello2()
print("v2=", v2)

