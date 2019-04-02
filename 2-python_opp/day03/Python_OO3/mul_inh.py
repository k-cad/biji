# mul_inh.py
# 多重继承示例
# 超人类继承自战士、飞行者、喷或者
# 三个类
class Fighter:  #战士类，默认继承自object
    def fight(self):
        print("我能战斗")

    def roar(self):  #吼叫
        print("战士吼叫：嗷嗷嗷")

class Flyer:  #飞行者类
    def fly(self):
        print("我能飞行")

    def roar(self):  #吼叫
        print("飞行者吼叫：呜呜呜")

class Firer: # 喷火者
    def fire(self):
        print("我能喷火")

# 超人类，继承自Fighter,Flyer,Firer父类
class SuperMan(Flyer,Fighter,Firer):
    pass

if __name__ == "__main__":
    super_man = SuperMan() # 实例化超人对象
    super_man.fight()  # 超人战斗
    super_man.fly()    # 超人飞行
    super_man.fire()   # 超人喷火
    super_man.roar()   # 超人吼叫？？
    # Mehtod Resolution Order
    # 决定调用哪一个类的方法
    # print(SuperMan.__mro__) 
    print(SuperMan.__bases__) # __bases__绑定父类
    print(Fighter.__base__)
    print(Flyer.__base__)
    