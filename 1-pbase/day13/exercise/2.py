def poker():
    import random
    l1=['\u2660','\u2663','\u2665','\u2666']
    l2=['A','2','3','4','5','6','7','8','9','10','J','K','Q']
    L1=[ x+y for x in l1 for y in l2]
    L2=['joker','Joker']
    pokes=L1+L2
    pokes1=pokes
    random.shuffle(pokes1)
    print(pokes1,len(pokes1))
    p1=pokes1[0:17]

    p2=pokes1[17:34]

    p3=pokes1[34:51]
    p4=pokes1[51:54]
    input()
    print(p1,'玩家一共%d张' % len(p1))
    input()
    print(p2,'玩家二共%d张' % len(p2))
    input()
    print(p3,'玩家三共%d张' % len(p3))
    input()
    print(p4,'剩余%d张' % len(p4))
    return

poker()
