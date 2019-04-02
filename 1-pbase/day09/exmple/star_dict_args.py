#star_dict_args.py
#此示例示意用双星号字典形参接受多余的关键字传参
def func(**kwargs):
    print('关键字传参的个数是：',len(kwargs))
    print("kwargs=",kwargs)

func(name='yy',age=22,address='beijing')
#func(a=1,b=2)