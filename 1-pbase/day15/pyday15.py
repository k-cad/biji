day15
生成器 genertor (python2.5及以后)
  什么是生成器
    生成器是能够动态提供数据的可迭带对象
    生成器在程序运行时生成数据,与容器类型不同，他通常不会在内存中保存大量的数据，而是现用现生成
  生成器有两种
    生成器函数
    生成器表达式
  生成器函数的定义
    含有yeild的语句的函数是生成器函数，此函数被调用将返回一个生成器对象
    (yield)产生生成
  yield语句
    语法：
        yield 表达式
    说明
        yield 用于def 函数中，目的是将此函数作为生成器函数使用
        yield 用来生成数据，供迭代器next()函数使用
    生成器函数说明
    1,生成器函数的调用将返回一个生成器对象，生成器对象是一个可迭代对象
    2,在生成器函数调用return会触发一个StopIteration异常(即生产数据结束)
    生成器表达式：
      语法：
          (表达式 for 变量 in 可迭带对象 [if 真值表达式])
      说明：
          if 子句可以省略
      作用：
          用推导式形式创建一个新的生成器
      示例：
          gen=(x**2 for x in range(1,5))
          it=iter(gen)#拿到迭代器
          print(next(it))#1
          print(next(it))#4
          print(next(it))#9
          print(next(it))#16
          print(next(it))#StopIteration
      说明：
          生成器通常是一次性的，当数据获取完成后不能再提供数据

迭代工具函数
    zip 函数
    enumerate 函数
zip 函数
    zip(iterel[,iter2,......]) 返回一个zip生成器对象，
    此对象用于生成一个元组，此元组的数据分别来自于参数中的每个可迭带对象，
    生成的元组个数由自小的可迭带对象大小决定
示例：
    numbers=[10086,10000,10010,95588]
    names=['中国移动','中国电信','中国联通']
    for t in zip(numbers,names):
        print(t)
    for n,na in zip(numbers,names):
        print(na,'的客服电话是：',n)
    
    d=dict(zip(numbers,names))#创造字典
    for t in zip(numbers,names,range(1,100000)):
        print(t)
    
    zip 函数的实现原理
        myzip.py
    enumerate 函数
       格式:
           enumerate(iterable,star=0)
       作用：
           生成一个枚举对象，此枚举对象生成的数据将原可迭带对象的数据
           与索引值形成元组(index,value)形式返回
       示例：
           L=[3,5,8,10]
           for i,v in enumerate(L):
               print('索引为',i,'元组的值为：',v)


字节串 和 字节数组(序列的种类：list str tuple)
字节串 bytes(也叫字节序列)
    作用：
        储存以字节为单位的数据
        字节串是不可改变的字节序列
    字节：
        字节是0~255 之间的整数，用来表示一个字节(8个位)的取值
        字节是数据存储的最小单位
    创建空字节串的字面值:
    B=b''
    B=b""
    B=b'''''''
    B=b""""""
    创建非空字节串的字面值：
    B=b'ABCD'
    B=b"ABCD"
    B=b'\x41\x42\x43\x44'
字节串的构造函数 bytes
    bytes() 生成一个空的字节串，等同于b''
    bytes(整数可迭带对象) 用可迭带对象初始化一个字节串
    bytes(整数n) 生成n个值为0的字节串
    bytes(字节串，encoding='utf-8') 用字符串转换编码生成一个字节串
示例：
    B=bytes()#B=b''
    B=bytes(range(65,69))#B=b'ABCD'
    B=bytes(10)#B=b'\x00\x00...'
    B=bytes('hello','uft-8')#B='hello'

bytes 的运算
   + += * *=
   < <= > >= == !=
   in / not in
   索引和切片

示例：
    b=b'abc123ABC'
    b'A' in b #True
    65 in b #True
    print(b(0))#97

函数
    len(x)
    max(x)
    min(x)
    sum(x)
    any(x)
    all(x)
bytes 与 str 的区别
    bytes 储存字节
    str 储存unicode字节
bytes 与 str 转换
    编码(encode)
str ----------> bytes
    b=s.encode(encoding='utf-8')
      解码(decode)
bytes ----------> str
    s=b.decode(encoding='utf-8')

字节数组 bytearray:可变的字节序列           不可变      可变的  (便于增删改查)
                                        tuple      list
                                        frozenset  set
                                        bytes      bytearray       
    
字节数组的构造函数 bytearray
  (同字节串)  
    bytearray() 生成一个空的字节数组，等同于b''
    bytearray(整数可迭带对象) 用可迭带对象初始化一个字节数组
    bytearray(整数n) 生成n个值为0的字节数组
    bytearray(字节数组，encoding='utf-8') 用字符数组转换编码生成一个字节数组

运算：
   + += * *=
   < <= > >= == !=
   in / not in
   索引和切片(字节数组的索引和切片可以赋值操作，规则同列表的索引和切片赋值规则相同)

方法参见文档

文件 file：
    文件是用于数据存储的单位
    文件通常用来长期存储数据
    文件中的数据以字节为单位进行顺序存储的
文件的操作流程：
    1，打开文件
    2，读写文件
    3，关闭文件
文件的打开和关闭
 文件需要在使用时先打开文件才能读写
 在不需要读写文件时，应及时关闭文件以释放系统资源
 任何操作系统，一个应用程序同时打开文件的数量有最大数限制
文件的打开函数
open(file,mode='rt') 用于打开一个文件，返回此文件对象
如果打开失败，则会触发OSError类型的错误
文件的关闭方法
F.close() 关闭文件，释放系统资源
文件文本的读取数据方法
F.read([n])
F.readline()
F.readlines()
文档参见

                                        