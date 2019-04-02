# test_mymod.py


# 此示例示意调用自定义的mymod.py 模块内的两个函数和两个字符串

import mymod  # 导入自定义模块 mymod.py

mymod.myfac(5)  # 调用自定义模块的函数
mymod.mysum(100) 

print(mymod.name1)  # 获取mymod里的name1绑定的字符串

from mymod import name2
print(name2)  # tesla

from mymod import *
myfac(20)
mysum(1000)

print("test_mymod.py里的__name__属性的值是:", __name__)
# __name__  = '__main__'