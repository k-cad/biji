#car.py
#继承示例，家用小汽车
from auto_mobile import *

#定义Car类，继承自AutoMobile类
class Car(AutoMobile):
    pass

if __name__=="__main__":
    mycar = Car('小汽车','蓝色',1.40)
    mycar.startup()
    mycar.run()
    mycar.stop()
    mycar.info()
    