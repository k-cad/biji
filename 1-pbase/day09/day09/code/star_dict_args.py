# star_dict_args.py

# 此示例示意用双星号字典形参接收多余的关键字传参

def func(**kwargs):
    print("关键字传参的个数是:", len(kwargs))
    print("kwargs=", kwargs)

func(name='weimingze', age=35, address='北京市朝阳区')
func(a=1, b=2)
