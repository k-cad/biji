from threading import Thread,Event
from time import sleep

s = None#全局变量用于通信
e = Event()
def foo():
    print("Foo coming")
    global s
    s = "open the door" 
    e.set()

f = Thread(target=foo)
f.start()

e.wait()
if s == "open the door":
    print('right')
else:
    print('wrong')

f.join()

