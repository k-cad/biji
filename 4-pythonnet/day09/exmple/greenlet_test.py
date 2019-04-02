from greenlet import greenlet

def test1():
    print('start test1')
    gr2.switch()
    print('end test1')

def test2():
    print('start test2')
    gr1.switch()
    print('end test2')

gr1 = greenlet(test1)
gr2 = greenlet(test2)

gr1.switch()






