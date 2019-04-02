# phone.py
# 手机类
import time
class Phone:
    def __init__(self, name, price, 
                 CPU, screen_size):
        self.name = name
        self.price = price
        self.CPU = CPU
        self.screen_size = screen_size

    def startup(self):
        print("正在开机")
        time.sleep(2)
        print("开机成功")

    def shutdown(self):
        print("正在关机")
        time.sleep(2)
        print("关机成功")

    def call(self, phone_no):
        print("正在拨号")
        time.sleep(1)
        print("正在和%s通话" % phone_no)

    def send_msg(self, phone_no, msg):
        print("正在向%s发送信息..." % phone_no)
        time.sleep(2)
        print("【%s】发送成功" % msg)

    def __del__(self):  # 析构方法
        print("__del__方法被调用")

def fun():
    phone = Phone("华为",1999.99,
                 "双核2G", 5.5)
    print("fun()函数退出")

if __name__ == "__main__":
    myphone = Phone("华为",1999.99,
                    "双核2G", 5.5)
    fun()   
    print("程序退出")
    # myphone程序退出时被销毁


 
    # myphone.startup()  #启动
    # myphone.call("13512345678") #打电话
    # myphone.send_msg("13512345678","你好")
    # myphone.shutdown()  #关机  