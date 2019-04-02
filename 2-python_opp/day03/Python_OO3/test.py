# test.py
# 测试程序
import ak47
import awp

ak = ak47.AK47("AK47", 30, 0, 0.4, 3) #实例化AK47对象
ak.reload()      #填弹
ak.fire()        #开火
ak.fire()
print("----------------")
awp = awp.AWP("AWP", 10, 0, 1.0, 1)  #实例化AWP对象
awp.reload()
awp.fire()

ak2 = ak47.AK47("AK47", 20, 0, 0.4, 3)