# gun.py
# 枪械类
class Gun:
    def __init__(self, name, max_bullets,
                 bullet_left,dest_ratio,
                firing_bullets):
        self.name = name  #名称
        self.max_bullets = max_bullets#弹夹容量
        self.bullet_left = bullet_left#剩余子弹
        self.dest_ratio = dest_ratio #杀伤系数
        # 每次开火击发子弹数量
        self.firing_bullets = firing_bullets
    
    def reload(self): # 填弹
        self.bullet_left = self.max_bullets
        print("填弹完成，剩余子弹%d发" % \
              self.bullet_left)

    def fire(self):  # 开火
        if self.bullet_left <= 0:#没子弹
            print("请填弹")
            return

        if self.bullet_left >= self.firing_bullets:
            self.bullet_left -= self.firing_bullets
        else: #剩余子弹小于一次击发打出的子弹
            self.bullet_left = 0 #全部打出

        # 计算杀伤力
        damage = int(self.dest_ratio*100)
        
        # 打印，模拟开火
        print("%s开火，杀伤力%d,剩余子弹%d" % \
          (self.name, damage, self.bullet_left))
