#写程序，实现以下要求：
# 1,将如下一个数据形成一个字典season
    # '键'        '值'
    # 1  ------  '春季有1,2,3月'
    # 2  ------  '夏季有4,5,6月'
    # 3  ------  '秋季有7,8,9月'
    # 4  ------  '冬季有10,11,12月'
    # 让用户输入一个整数代表这个数字，打印这个季度的信息
    # 如果用户输入的信息不存在，则打印'信息不存在'

# season={
#     1:'春季有1,2,3月',
#     2:'夏季有4,5,6月',
#     3:'秋季有7,8,9月',
#     4:'冬季有10,11,12月'
#     }
season={}
season[1]='春季有1,2,3月'
season[2]='夏季有4,5,6月'
season[3]='秋季有7,8,9月'
season[4]='冬季有10,11,12月'
n=int(input('请输入季度：'))
if n  in season:
    print(season[n])
else:
    print('信息不存在')

