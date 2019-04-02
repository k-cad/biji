#   1. 一个球从100米高空落下，每次落地后反弹高度为原高度的一半，再
#     落下,写程序算出:
#        1) 皮球在第10次落地后反弹的高度
#        2) 皮球在第10次落地反弹后共经历多少米路程

def get_last_height(height, times):
    '''height 原来的高度 
       times 为反弹次数'''
    for _ in range(times):
        height /= 2  # 每次反弹高度为原高度的一半
    return height
    
print("皮球从100米高度落下反弹十次后高度为:",
      get_last_height(100, 10))


def get_distance(height, times):
    meter = 0  # 用来记录总路程
    for _ in range(times):
        # 累加下落过程的路程
        meter += height
        height /= 2 # 计算返回后的高度
        # 累加反弹之后的路程
        meter += height
    return meter

print("皮球从100米高度落下反弹十次后的总路程为:",
    get_distance(100, 10))