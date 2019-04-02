from bird import *
class Eagle(Bird):
    def eat(self):
        print('%s是肉食类的动物' % self.name)
    def wing(self):
        print('翅膀长达3米')
        