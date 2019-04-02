day15回顾
生成器
    能够动态提供数据的对象(现用现生成)
    两种生成器
       生成器函数
           含有yield语句的函数为生成器函数,此函数调用将返回生成器
           生成器是可迭带对象
               def myyield():
                   yield 1
                   yield 3
               next(it)  函数将会让生成器函数执行
            生成表达式
                (表达式 for 变量列表 in 可迭带对象 if 真值表达式)
    字节串 字节数组
        字节串 bytes (不可变)
        字节数组 bytes (可变)
        len(x) max(x) 
    文件的读取操作
day16 
文本文件的写操作
 open(文件路径名,mode='rt')
 mode  模式字符串的含义
 r     读read
 t     文本
 w     写write
 x     创建新文件如果文件存在则报错
 a     追加append

 文本文件操作
 模式字符
 't'(默认)
 说明：
 1,对文本文件的读写，需要用字符串(str) 进行读取和写入操作
 2,默认文件中储存的都为字符数据，在读写中会自动进行编解码转换操作
 3，以行为单位分隔，在python内部统一用'\n'作为换行符进行分隔
 各操作系统的换行符
 windows \r\n
 linux    \n
 mac os    \n

 文本文件的迭代读取
    文件流对象是可迭带对象，迭代过程中将以换行符'\n'作为分隔符依次获取
 示例 f= open('./mynote.txt')
      for line in f:
          print(line)


标准输入输出文件
  sys.stdin 标准输入文件(ctrl + d 输入文件结束符)
  sys.stdout 标准输出文件
  sys.stderr 标准错误输出文件
  注： 标准文件不需要打开和关闭就可以使用
  示例见：
  stdout.py

二进制文件操作
   二进制文件操作模式字符
       'b'
   说明：
       1,默认文件中储存的都是以字节(byte)为单位的数据通常有人为规定的格式
       2，对二进制文件的读写操作学要用字节串(bytes)进行操作

   二进制文件以字节(byte)为单位储存和读写操作，不以字节串为单位进行读写的文件方式

读方法
    F.read()
    对于文本文件，F.read()返回类型为字符串(str)
    对于二进制文件 则返回字节串(bytes)
写方法：
    F.write(x)
    二进制模式是，x必须是字节串
    文件模式时，x必须是字符串

F.tell() 方法
作用：返回当前文件的读写位置(从文件头以字节为单位的整数)
见：tell.py
F.seek 方法
作用：设置文件的读写位置
格式：
    F.seek(偏移量,whence=相对位置)
    偏移量：
          大于0的数代表向文件末尾方向移动
          小于0代表向文件头移动
    相对位置
          0 代表从文件头开始偏移
          1 代表从当前读写位置开始偏移
          2 代表从文件尾开始偏移
F.flush方法
  作用：
      清空缓存区
  格式：
      F.flush()

  
文件操作：
1，文本文件操作(以字符串为单位进行操作，自动编码解码) 't'
2,二进制文件方式(以字节串为单位进行操作，不进行编解码) 'b'
IO操作(input 读,output 写)
读操作 'r'
     F.read()
     F.readline()
     F.readlines()
写操作 'w' 'x' 'a'
     F.write()
     F.writeline()
关闭操作
  F.close()
文件读写位置的定位操作
  F.tell()
  F.seek()
清空缓存区操作
 F.flush()
汉字编码
    国标系列：
     GB18130(收录27533个汉字，二字节或四字节)
        GBK(收录21003个汉字，二字节)
           GB2313(收录6763个汉字 + 682个全角符号，二字节)
     windows常用
    国际标准：
       Unicode32(32位表示的文字编码)
            Unicode16(16位表示的文字编码)
        (Linux /Mac OS X/IOS,Android))
    UTF-8
        UTF-8(8-bit Unicode Transformation Format)
            0x0000 ~ 0x007F 一字节编码
            0x0080 ~ 0x07FF 二字节编码
            0x0800 ~ 0xFFFF 三字节编码

python 编码转化字符串
    'gb2313'
    'gbk'
    'gb18030'
    'utf-8'
    'ascii'
    用于s.encode(x) 和 b.decode(x)中
    如：
s='十个汉字多少个字节'
print(s.encode('gbk'))
print(s.encode('utf-8'))
       
编码注释：
     在源文件的第一行或第二行写入如下内容为编码注释
     # -*- coding:gbk-*-
     或
     # -*- coding:utf-8 -*-
    作用：
    指示python3解释进行器当前文件的编码是什么