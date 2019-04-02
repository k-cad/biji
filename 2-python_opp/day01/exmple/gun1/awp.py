#awp.py
#狙击枪
class AWP:
    def __init__(self):
        self.name = 'AWP' #名称
        self.max_bullets = 10 #弹夹容量
        self.bullet_left = 0 #剩余子弹
        self.destructRatio = 1.0 #杀伤系数
    
    def reload(self):   #填弹
        # 填弹后，剩余子弹数等于担架容量
        self.bullet_left = self.max_bullets
    
    def fire(self): #开火
        if self.bullet_left <= 0:#没子弹
            print('请填弹')
            return
        #计算剩余子弹
        self.bullet_left -= 1
        damage = int(self.destructRatio*100)
        print('嘣，杀伤力%d,剩余子弹%d' %
              (damage,self.bullet_left))    
        