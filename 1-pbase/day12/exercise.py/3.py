
def alarm(hour,minute):
    import time
    while True:
        t=time.localtime()
        print('%02d:%02d:%02d'%t[3:6],end='\r')
        time.sleep(0.1)
        if t[3:5]==(hour,minute):
            print('时间到！')
            return

h=int(input('请输入小时：'))
m=int(input('请输入分钟：'))    
alarm(h,m)