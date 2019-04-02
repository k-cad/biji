# car.py
# 家用小汽车类，继承示例
from auto_mobile import *

# 定义Car类，继承自AutoMobile类
class Car(AutoMobile): 
    pass

if __name__ == "__main__":
    mycar = Car("小汽车", "蓝色", 1.40)
    mycar.startup()  #启动
    mycar.run()      #行驶
    mycar.stop()     #停止
    mycar.info()     #打印信息
