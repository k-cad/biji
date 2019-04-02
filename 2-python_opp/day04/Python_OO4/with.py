# with.py
# with语句示例
# try:
#     #f = open("aaa.txt", "rt")
#     # 使用with语句，不管以下的操作是否
#     # 发生异常，都能保证文件被正确关闭
#     with open("a.txt", "rt") as f:
#         for line in f:
#             print(line,end="")
#     # with语句结束
# except:
#     print("文件操作失败")

class A:  #自定义资源管理器
    def __init__(self, name):
        self.name = name

    def __enter__(self): 
        print("__enter__()方法被执行")
        return self

    def __exit__(self, exc_type, exc_val,exc_tb):
        print("__exit__()方法被执行")
        if exc_type is None: #没有出现异常
            print("没有出现异常")
        else: # 出现异常
            print("错误类型:", exc_type)
            print("错误对象:", exc_val)
            print("TraceBack:", exc_tb)

if __name__ == "__main__":
    with A("test_name") as a:
        print("with语句执行了")
        # 制造或不制造异常
        a = int(input("请输入一个数字:")) 

    print("程序退出")