# ctrl_c.py

try:
    import time
except ImportError:
    print("导入时间模块失败!")

try:
    while True:
        time.sleep(1)
        print(time.asctime())
except KeyboardInterrupt:
    pass

print("程序正常退出")

