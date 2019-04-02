# with.py
# try:
#     # f = open('a.txt','rt')
#     with open('a.txt','rt') as f:
#         for line in f:
#             print(line,end='')

# except:
#     print('文件操作失败')

class A:#自定义资源管理器
    def __init__(self,name):
        self.name = name

    def __enter__(self):
        print("__enter__语句被执行")
        return self

    def __exit__(self,exc_type,exc_val,exc_tb):
        print('__exit__语句执行了')
        if exc_type is None:
            print('没有出现异常')
        else:
            print("错误类型:",exc_type)
            print("错误对象:",exc_val)
            print("TraceBack:",exc_tb)

if __name__ == "__main__":
    with A("test_name") as a:
        print('with语句执行了')
        a = int(input('请输入一个数字'))
    print("程序退出")

