#外部嵌套函数内的变量保存压岁钱
def gm(money):
    def cb(obj,m):
        nonlocal money
        if money >m:
            money -= m
            print(m,money)
        else:
            print(0)
    return cb
