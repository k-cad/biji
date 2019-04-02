#   2. 模拟斗地主发牌，牌共54张
#     种类:
#       黑桃('\u2660'), 梅花('\u2663'), 方块('\u2665'),
#       红桃('\u2666')
#     数字:
#        A2-10JQK
#     王牌: 大小王
#     三个人，每人发17张牌，底牌留三张
#     输入回车，打印第1个人的17张牌
#     输入回车，打印第2个人的17张牌
#     输入回车，打印第3个人的17张牌
#     输入回车，打印3张底牌

poke = ['大王', '小王']

kinds = ['\u2660', '\u2663', '\u2665', '\u2666']
numbers = ['A']
numbers += [str(x) for x in range(2, 11)]
numbers += list("JQK")

for k in kinds:
    for n in numbers:
        poke.append(k + n)
# poke += [k + n for k in kinds for n in number]

# print(poke)
assert len(poke) == 54, '出错'
# 打乱
poke2 = poke.copy()
import random
random.shuffle(poke2)

player1 = poke2[:17]
player2 = poke2[17:34]
player3 = poke2[34:51]
base = poke2[51:]

input()
print("打印第1个人的17张牌:", player1)
input()
print("打印第2个人的17张牌:", player2)
input()
print("打印第3个人的17张牌:", player3)
input()
print("三张底牌:", base)



