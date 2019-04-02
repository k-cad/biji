# closure_make_power.py
# 写一个求x的平方的函数
def make_power(y):
    def fn(x):
        return x**y
    return fn

pow2=make_power(2)
print('五的平方式',pow2(5))
pow3=make_power(3)
print(pow3(7))                    