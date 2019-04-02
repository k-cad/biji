# mydecol.py

def mydecol(fn):
    def fx():
        print('++++++++')
        fn()
        print('--------')
    return fx
@mydecol
def myfunc():
    '''被装饰函数'''
    print('此函数被调用')

# myfunc=mydecol(myfunc) #等同于@mydecol
myfunc()