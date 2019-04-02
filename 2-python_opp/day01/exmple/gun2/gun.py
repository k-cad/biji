#gun.py
#枪械类
class Gun:
    def __init__(self,name,max_bullets,bullet_left,dest_ratio,firing_bullets):
        self.name=name
        self.max_bullets = max_bullets
        self.bullet_left = bullet_left
        self.dest_ratio = dest_ratio
        # 每次开火击发子弹数量
        self.firing_bullets = firing_bullets

    def reload(self):
        self.bullet_left=self.max_bullets
        print('填弹完成，剩余子弹%d发'%self.bullet_left)        

    def fire(self):
        if self.bullet_left == 0:
            print('请填弹')
            return
        
        if self.bullet_left  >= self.firing_bullets:
            self.bullet_left -= self.firing_bullets
        else:
            self.bullet_left = 0
    
        damage = int(self.dest_ratio*100)

        print('%s开火,杀伤力%d,剩余子弹%d' % 
              (self.name,damage,self.bullet_left))

        

