#多重继承示例
# 超人类继承自战士,飞行者,喷火者三类
class Fighter:
    def fight(self):
        print('我能战斗')

class Firer:
    def fire(self):
        print('我能喷火')
    
    def roar(self):
        print('hahhaha')

class Flyer:
    def fly(self):
        print('我能飞行')
    def roar(self):
        print('heiheihei')

class SuperMan(Fighter,Flyer,Firer):
    pass

if __name__=="__main__":
    super_man = SuperMan()
    super_man.fight()
    super_man.fly()
    super_man.fire()
    super_man.roar()

#method resolution order
print(SuperMan.__mro__)
print(SuperMan.__base__)
print(Fighter.__base__)