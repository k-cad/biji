# named_keywords_args.py
#此示例示意在函数形参中定义命名关键字形参，强制让函数调用使用命名关键字传参
def func1(a,b,*agrs,c,d):
    print(a,b,c,d)

func1(1,2,3,4)
func1(1,2,c=30,d=40)
func1(a=10,b=20,c=30,d=40)
