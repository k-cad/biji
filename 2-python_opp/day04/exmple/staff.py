#员工类,演示__slots__属性
class Staff:
    __slots__ = ['NO','name','position']

    def __init__(self,NO,name,position):
        self.NO = NO
        self.name = name
        self.position = position
        # self.salary = 8000#不允许

    def __str__(self):
        ret = '编号:%s,姓名:%s,职位:%s'\
            %(self.NO,self.name,self.position)
        return ret
    
    def work(self):
        print('%s正在工作'%self.name)

#定义机器人继承Ｓｔａｆｆ类
class ServiceRobot(Staff):
    def __init__(self,NO,name,position):
        super().__init__(NO,name,position)

    def work(self):
        print('%s的工作,扫地'%self.name)


if __name__ == "__main__":
    staff = Staff('00001','Jerry','Manager')
    print(staff)
    robot = ServiceRobot('00002','多来阿蒙','服务员')
    print(robot)
    robot.work()


