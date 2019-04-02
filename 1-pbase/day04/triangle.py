w = int(input('请输入:'))
stars = w
while stars <= w:
    blank=w-stars
    print(' '*blank+'*'*stars)
    stars += 1
print('------')
stars=w
while stars > 0:
    blank=w-stars
    print(' '*blank+'*'*stars)
    stars -=1
print('------')
stars=w
while stars >0:
    blank = w - stars
    print('*'*stars)
    stars -=1
print('------') 