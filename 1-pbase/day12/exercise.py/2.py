

def show_time():
    import time
    while True:
        t=time.localtime()
        print('%02d:%02d:%02d' % t[3:6],end='\r')
        # print('%02d:%02d:%02d' % (t[3],t[4],t[5]),end='\r')
        time.sleep(0.1)

show_time