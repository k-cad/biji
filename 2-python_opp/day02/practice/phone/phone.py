import time
class Phone:
    def __init__(self,name,price,CPU,screen_size):
        self.name = name 
        self.price = price
        self.CPU = CPU
        self.screen_size = screen_size

    def startup(self):
        print('%s欢迎您...' % self.name)
        time.sleep(2)
        print('开机成功')

    def shutdown(self):
        print('您的%s正在关机' % self.name)
        time.sleep(2)
        print('关机机成功')
    
    def call(self):
        no=int(input('请输入您要拨打的号码'))
        print('正在拨号')
        time.sleep(1)
        print('正在和%d通话' % no )
    
    def send_msg(self):
        msg=str(input('请编辑短信：'))
        no = int(input('发送给：'))
        print('正在向%d发送短信' % no) 
        time.sleep(2)
        print('发送成功')   
    def __del__(self):
        print('__del__方法被调用')

if __name__ == "__main__":
    myphone = Phone('iPhone',5899,'四核8G',5.0)
    myphone.startup()
    myphone.call()
    myphone.send_msg()
    myphone.shutdown()
    
        print('__del__方法被调用')