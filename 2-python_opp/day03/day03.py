1.多态
 1)什么是多态:同一个方法，在不同子类中有不同的表现
 2)方法的重写来实现
 3)保持程序的扩展性,灵活性
2.面向对象的技术特性
 1)构造方法与析构方法
  a)构造:__init__()
    调用时机:对象被创建时自动调用
    作用:创建对象属性,并赋值
    注意:子类构造方法显示调用父类构造方法
  b)析构方法:__del__()
    调用时机:对象被销毁时调用
    作用:对象销毁时执行清理操作
  2)object类:所有类的父类
             如果类定义时没有指定父类
             默认从object中继承
             __base__查看父类
  3)super()和issubclass()
    super():获得绑定的父类
        格式:super() 只能在类方法中使用
            super(type,obj) 返回obj的父类
    issubclass():判断某个是不是另一个类的子类
        格式:issubclass(cls,cls_or_tuple)

  4)多重继承:一个类有多个父类
    MRO:方法解析顺序,__mro__属性
        从下至上，从左至右
3.函数的重写:让对象操作更方便
  1)对象转字符串函数
    str():__str__(),返回字符串给人阅读
    repr():__repr__(),返回字符串给解释器阅读
  2)内建函数:
    abs():__abs__()
    len():__len__()
    reversed():__reversed__()
    round():__round__()
  3)数值转换函数
    int():__int__()
    float():__float__()
    complex():__complex__()
    bool():__bool__()
  4)属性操作函数
    getattr(obj,name):获取对象属性
    setattr(obj,name,value):设置某个属性值
    hasattr(obj,name):判断对象有没有某个属性值
    delattr(obj,name):删除某个属性值

day03 笔记
可迭代对象
1)什么是迭代器
2)代码特征: 重写__iter__方法返回可迭对象
           重写__next__方法获取下一个元素
3)__next__()方法，实现迭代器协议
  如果有下一个元素,则返回
  如果没有下一个元素，则抛出StopIteration异常
示例见 myiter.py

2.运算符重载
1)运算符重载:自定义类中，重写某些方法，重写
  后就可以对对象进行某些运算符操作
2)目的
  a)简化对象操作
    如:
    c = "abc" +"123"
    d = "123" > "456"
  b)代码清晰,直观
  c)可以在类中自定义运算规则
  注意:运算加载不要改变原有意义
  
	 注意：运算重载不要改变原有意义
 
  3）算术运算符重载
    - 重写方法后,支持+,-,*,//,/,%,**
	- 重载方法和运算符的对应关系
	  __add__(self,rhs)   self + rhs
	  __sub__(self,rhs)   self - rhs
	  __mul__(self,rhs)   self * rhs
	  __truediv__(self,rhs)   self / rhs
	  __floordiv__(self,rhs)  self // rhs
	  __mod__(self,rhs)       self % rhs
	  __pow__(self,rhs)       self ** rhs
  
  课堂练习:在MyList类中,重载+,*运算符
          L1 = MyList([1,2,3])
		  L2 = MyList([4,5,6])
		  L1 + L2==>MyList([1,2,3,4,5,6])
		  L1*2 ==> MyList([1,2,3,1,2,3])
          见mylist.py
		  
	4）反向算术运算符重载
	   在正向运算符重载的函数前面加r
	   例如：__radd__(), __rsub__()...
	   支持：2 + obj (对象在操作符右边)

	5）复合运算操作符
	   在正向运算符重载的方法前加i前缀
	   例如：__iadd__(), __isub__()...
	   重载运算符后，执行复合表达式
	   ojb += 2，首先查找__iadd__()，
	   如果没有找到，则再查找__add__()，
	   如果再没有找到，报TypeError异常
	   
	6）比较运算符：>,<,>=,<=,==,!=
	  - 重写方法和运算符的对照关系
	    __lt__(self, rhs)   self < rhs
	    __gt__(self, rhs)   self > rhs
	    __eq__(self, rhs)   self == rhs
	    __ne__(self, rhs)   self != rhs
	    __ge__(self, rhs)   self >= rhs
	    __le__(self, rhs)   self <= rhs
	  - 示例：见truck.py
	  - 比较规则：
	    >: 首先找__gt__(), 没有找__lt__()
		   并将执行__lt__()结果取反
		   如果__lt__()不存在则报错
		<: 规则和大于相反
		>=:首先找__ge__(), 没有找__le__()
		   并将执行__le__()结果取反
		   __le__()不存在则报错
		<=:规则和大于等于相反 
		==:首先找__eq__(), 如果不能存在则
		   判断两个对象ID值，相同返回True
		   不同返回False
		!=:首先找__ne__(),不存在则找
		   __eq__()并执行取反
		   如果__eq__()不存在则比较ID
		   ID相同返回False，否则返回True
	  
	课堂练习：在MyList类中，重载>,<,==,!=
	  操作符，比较规则如下：
	  等于：data属性元素个数相等
	        并且相同位置上的值相等
	  大小比较：[1,2,4] > [1,2,3]
	            [1,2,3,4] > [1,2,3]
				[1,2,4] > [1,2,3,4]
	  代码见：mylist.py	
	  
    7）一元运算符：带一个操作数的操作符
	  __neg__(self)   -self  负号运算
	  __pos__(self)   +self  正号运算
	  __invert__(self) ~self 取反运算
	  
	  作用：重写上述方法，支持对象如下操作：
	        -obj, +obj, ~obj
			
	8）in/not in运算符重载
	   只需要重载__contains__(self,e)
	   in运算，则直接调用__contains__()
	   not in运算，调用__contains__()取反
	
	9）索引运算符重载:支持[]操作
	   __getitem__(self,i)       self[i]
	   __setitem__(self,i,value) self[i]=value
	   __delitem__(self,i)       del self[i]

3. 实例的内置属性
  1）__dict__属性：绑定实例自身的变量字典
     包括父类创建的属性和私有属性
     示例：
     am = AutoMobile("卡车","blue",4.0)
	 print(am.__dict__)
	 
  2）__class__属性：绑定创建该对象的类
	 
作业：	
1）编写一个汽车租赁程序，包含汽车类(Car),
客户类(Customer), 租车店类(CarStore),各个
类包含的属性和方法有：
	Car类：
		属性
		car_id	车辆id号
		name	车辆名称
		is_lend	是否出租
		price	每天单价
		start_date	起租日期
		end_date	租赁终止日期
		方法
		__str__()
		
	Customer类：
		属性
		cust_id		客户编号
		cust_name	客户姓名
		tel_no		客户电话
		方法
		__str__()
	CarStore类：
		属性
		cars		所有车辆列表
		customers	所有客户列表
		方法
		__load_cars()	加载所有车辆信息
		__load_customers()	加载所有客户信息
		print_cars_info()	打印所有车辆信息
		find_car()			查找车辆
		add_car()			添加车辆
		del_car()			删除汽车
		lend()				租车
		back()				还车
2）实现上述类，并编写测试代码
	
# 作业：	
# 1）编写一个汽车租赁程序，包含汽车类(Car),
# 客户类(Customer), 租车店类(CarStore),各个
# 类包含的属性和方法有：
# 	Car类：
# 		属性
# 		car_id	车辆id号
# 		name	车辆名称
# 		is_lend	是否出租
# 		price	每天单价
# 		start_date	起租日期
# 		end_date	租赁终止日期
# 		方法
# 		__str__()
		
# 	Customer类：
# 		属性
# 		cust_id		客户编号
# 		cust_name	客户姓名
# 		tel_no		客户电话
# 		方法
# 		__str__()
# 	CarStore类：
# 		属性
# 		cars		所有车辆列表
# 		customers	所有客户列表
# 		方法
# 		__load_cars()	加载所有车辆信息
# 		__load_customers()	加载所有客户信息
# 		print_cars_info()	打印所有车辆信息
# 		find_car()			查找车辆
# 		add_car()			添加车辆
# 		del_car()			删除汽车
# 		lend()				租车
# 		back()				还车
# 2）实现上述类，并编写测试代码
	
# 	CarStore类：
# 		属性
# 		cars		所有车辆列表
# 		customers	所有客户列表
# 		方法
# 		__load_cars()	加载所有车辆信息
# 		__load_customers()	加载所有客户信息
# 		print_cars_info()	打印所有车辆信息
# 		find_car()			查找车辆
# 		add_car()			添加车辆
# 		del_car()			删除汽车
# 		lend()				租车
# 		back()				还车






















