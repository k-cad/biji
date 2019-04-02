# mymod3.py

# 此示例示意模块的隐藏属性,当此模块用from import * 语句导
# 入时,不会导入 _f, __f, 和 _name 属性

def f():
    pass

def _f():
    pass

def __f():
    pass

name = 'aaa'
_name = 'bbb'
