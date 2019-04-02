

def play():
    print('正在玩魂斗罗！')

def gameover():
    print('gameover!')
    #调用上一级文件夹里的menu.py里的show_menu函数
    #用绝对导入函数
    # from mypack.menu import show_menu
    #用相对导入方式
    from ..menu import show_menu
    show_menu
    #调用tanks.py 里的 play()函数
    from .tanks import play
    tanks.play()
    #或
    from .tanks import play
    play()
print('魂斗罗加载中！！！')