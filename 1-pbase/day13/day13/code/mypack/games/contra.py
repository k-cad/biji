# file: mypack/games/contra.py


def play():
    print("正在玩魂斗罗...")

def gameover():
    print("魂斗罗游戏结束!!!")
    # 调用上一层文件里的menu.py 里的show_menu函数

    # 用绝对导入的方式:
    # from mypack.menu import show_menu

    # 用相对导入方式
    from ..menu import show_menu
    show_menu()  #  调用 

    # 相在此处调用tanks.py 里的 play() 函数怎么导入?
    # 1. 
    # import mypack.games.tanks as tanks
    # tanks.play()

    # 2.
    # from mypack.games.tanks import play
    # play()

    # 3.
    # from .tanks import play
    # play()

    # 4.
    from ..games.tanks import play
    play()

    # 5.  出错
    # from ...mypack.games.tanks import play
    # play()

print("魂斗罗模块被加载!!!")

