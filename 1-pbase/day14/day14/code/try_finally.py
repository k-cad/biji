# try_finally.py

# 此示例示意try_finally语句的作用

def fry_egg():
    print("打开天燃气...")
    try:
        count = int(input("请输入鸡蛋个数: "))
        print("完成煎鸡蛋，共煎了%d个鸡蛋" % count)
    finally:
        print("关闭天燃气!")

try:
    fry_egg()
except ValueError:
    print("煎蛋过程中出错！！！！")
