

def fry_egg():
    try:
        print('打开天然气')
        try:
            count=int(input('请输入鸡蛋个数：'))
            print('完成煎鸡蛋，共煎了%d个蛋'%count)
        finally:
            print('关闭天然气')
    except ValueError:
        print('煎蛋过程出错！')

fry_egg()

