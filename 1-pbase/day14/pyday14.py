day14
异常(基础) exception
    什么是错误
        错误是指由于逻辑或语法特异致一个程序无法正常执行的问题
    错误的特点
        无法预知
    什么是异常
        异常是程序出错时标识的一种状态
        当异常发生时，程序不会在向下执行，而转用调用此函数的地方待处理此错误并恢复为正常状态
    作用
        用作信号，通知上层调用者有错误产生需要处理
try 语句的两种语法
    try-except 语句
    try-finally 语句
try-except
语法
    try:
        可能触发异常的语句
    except 错误类型 [as 变量]:
        异常处理语句
    except 错误类型 [as 变量]:
        异常处理语句
    except 错误类型 [as 变量]:
        异常处理语句
    ...
    except:
        异常处理语句other
    else:
        未发生异常语句
    finally:
        最终语句
作用：
    尝试捕获异常错误，得到异常通知，将程序由异常流程转为正常流程并继续执型
说明：
    as 子句是用于绑定错误对象的变量，可省略
    except 子句可以有一个或多个，但至少要有一个
    else 子句最多只能有一个，也可以省略不写
    finally 子句最多只能有一个，也可以省略不写
示例见：try_except.py
python3 中的全部错误类型
参见文档 python_base_
Ctrl + C 
查看全部的类型
    help(__builtins__)
try-finally
    语句
      try:
          可能触发异常的语句
      finally:
          最终语句
    说明:
        finally 子句不可以省略
        一定不存在except子句
    作用:
        1,通常用try.finally 语句来做触发异常时必须要处理的事情
          无论异常是否发生，finally子句都会被执行
    注：
       try-finally 语句不会改变程序的(正常/异常)状态

raise 语句
  作用：
      触发一个错误，让程序进入一个异常状态
      发送错误通知给调用者
  语法：
      raise 异常类型
      或
      raise 异常对象
      或
      raise #重新触发上一次异常
  示例：
      raise.py

asert 语句(断言语句)
  语法:
      assert 真值表达式，错误数据(通常是字符串)
  作用：
  当真值表达式为False,用错误数据创键一个AssertionError
  类型的错误，并进入异常状态
  等同于：
   if bool(真值表达式)==False:
       raise AssertionError(错误数据)
  等同于：
   if bool(真值表达式)==False:
       raise AssertionError(错误数据)
  示例见：
       assert.py

为什么要用异常处理机制
  在程序调用层数较深时，向主调用函数传递错误信息需要层层返回比较麻烦，所以需要异常处理机制

迭代器 Iterator
    什么是迭代器
        迭代器是访问可迭代对象的工具
        是指iter(obj) 函数返回的对象
        可以用next(it) 函数获取可迭带对象的数据
    函数
        iter(iterable) 从可迭代对象中返回一个迭代器
        iterable 必须是一个可以提供一个迭代器的对象
        next(iterator) 从迭代器iterator中获取下一个对象，如果无法
        获取下一条记录，则触发StopIteraton异常
    说明：
        迭代器只能往前取值，不会后退
        用iter函数可以返回一个可迭代对象的迭代器
    示例：
        L=[2,3,7,5]
        it = iter(L)
        print(next(it))#2
        print(next(it))#3
        print(next(it))#7
        print(next(it))#5
        print(next(it))#StopIteration
    迭代器的用途：
        迭代器对象能用next函数获取下一个元素，可以用迭代器对任何的可迭带对象进行访问和遍历
    示例见：
    iterator.py
    L=[2,3,5,7]
    for in 语句实质是while语句+迭代器+try语句的组合
    